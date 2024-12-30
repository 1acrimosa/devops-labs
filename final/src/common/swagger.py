import logging
from collections import namedtuple

from django.utils.translation import gettext
from drf_yasg.inspectors import SwaggerAutoSchema as DrfYasgSwaggerAutoSchema
from rest_framework.permissions import OperandHolder, SingleOperandHolder


def _stringify_permission_class(permission_class):
    if isinstance(permission_class, OperandHolder):
        left, left_needs_brackets = _stringify_permission_class(permission_class.op1_class)
        right, right_needs_brackets = _stringify_permission_class(permission_class.op2_class)
        left = left if not left_needs_brackets else "(%s)" % left
        right = right if not right_needs_brackets else "(%s)" % right
        return "%s %s %s" % (left, permission_class.operator_class.__name__, right), True
    elif isinstance(permission_class, SingleOperandHolder):
        exp, needs_brackets = _stringify_permission_class(permission_class.op1_class)
        exp = exp if not needs_brackets else "(%s)" % exp
        return "%s %s" % (permission_class.operator_class.__name__, exp), True
    else:
        return get_permission_class_name(permission_class), False


def stringify_permission_class(permission_class):
    return _stringify_permission_class(permission_class)[0]


def get_permission_class_name(permission_class):
    if hasattr(permission_class, "display_name"):
        return permission_class.display_name
    if hasattr(permission_class, "__name__"):
        return permission_class.__name__
    return "UNKNOWN"


def get_permission_class_docs(permission_class):
    if hasattr(permission_class, "__doc__"):
        if permission_class.__doc__ is not None:
            return permission_class.__doc__
    return "NO DESCRIPTION"


PermissionItem = namedtuple("PermissionItem", ["name", "doc_str"])

logger = logging.getLogger(__name__)


def _render_permission_item(item):
    return f"+ `{item.name}`: *{item.doc_str}*"


def _handle_permission(permission_class) -> PermissionItem:
    permission_item = PermissionItem(
        get_permission_class_name(permission_class),
        get_permission_class_docs(permission_class).replace("\n", " ").strip(),
    )
    return permission_item


def _get_permissions_expression_markup(permission_classes):
    parts = []

    for permission_class in permission_classes:
        exp, needs_brackets = _stringify_permission_class(permission_class)
        parts.append(exp if not needs_brackets else "(%s)" % exp)

    return "\n`%s`\n" % (" AND ".join(parts))


def _traverse_permission_class(permission_class, permission_classes):
    if isinstance(permission_class, OperandHolder):
        _traverse_permission_class(permission_class.op1_class, permission_classes)
        _traverse_permission_class(permission_class.op2_class, permission_classes)
    elif isinstance(permission_class, SingleOperandHolder):
        _traverse_permission_class(permission_class.op1_class, permission_classes)
    else:
        permission_classes.add(permission_class)


def _get_permissions_list_markup(permission_classes):
    permissions = set()

    for permission_class in permission_classes:
        _traverse_permission_class(permission_class, permissions)

    permission_items = [
        _render_permission_item(_handle_permission(permission)) for permission in permissions
    ]

    return "\n\n".join(sorted(permission_items))


class SwaggerAutoSchema(DrfYasgSwaggerAutoSchema):
    """View inspector with some project-specific logic."""

    def get_summary_and_description(self):
        """Return summary and description extended with permission docs."""
        summary, description = super().get_summary_and_description()
        permissions_description = self._get_permissions_description()
        if permissions_description:
            description += permissions_description
        return summary, description

    def _get_permissions_description(self):
        if getattr(self.view, "get_permission_classes", None) is not None:
            permission_classes = self.view.get_permission_classes()
        else:
            permission_classes = getattr(self.view, "permission_classes", [])

        if len(permission_classes) > 0:
            return gettext(
                """
            \n\n**Permission logic:**\n%s\n
            \n\n**Permission references:**\n%s\n
            """
                % (
                    _get_permissions_expression_markup(permission_classes),
                    _get_permissions_list_markup(permission_classes),
                )
            )
        else:
            return None
