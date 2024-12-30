import logging

from rest_framework import status
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from common.api.responses import OKResponse
from common.api.serializers import validate_serializer_or_raise_exception

logger = logging.getLogger(__name__)


class BaseMixin:

    serializer_classes: dict = {}

    def get_serializer_class(self):
        if self.action in self.serializer_classes:
            return self.serializer_classes.get(self.action)
        raise NotImplementedError("No serializer class for action: %s." % self.action)

    def get_serializer_class_for_action(self, action):
        if action in self.serializer_classes:
            return self.serializer_classes.get(action)
        raise NotImplementedError("No serializer class for action: %s." % action)


class DefaultCreateModelMixin(BaseMixin, CreateModelMixin):
    """
    Create a model instance.
    """

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        validate_serializer_or_raise_exception(serializer)
        instance = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        retrieve_serializer = self.get_serializer_class_for_action("retrieve")(
            instance, context=self.get_serializer_context()
        )
        return OKResponse(retrieve_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class DefaultListModelMixin(BaseMixin, ListModelMixin):
    """
    List a queryset.
    """

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return OKResponse(serializer.data)


class DefaultRetrieveModelMixin(BaseMixin, RetrieveModelMixin):
    """
    Retrieve a model instance.
    """

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return OKResponse(serializer.data)


class DefaultUpdateModelMixin(BaseMixin, UpdateModelMixin):
    """
    Update a model instance.
    """

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        validate_serializer_or_raise_exception(serializer)
        instance = self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        retrieve_serializer = self.get_serializer_class_for_action("retrieve")(
            instance, context=self.get_serializer_context()
        )

        return OKResponse(retrieve_serializer.data)

    def perform_update(self, serializer):
        return serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)


class DefaultDestroyModelMixin(BaseMixin, DestroyModelMixin):
    """
    Destroy a model instance.
    """

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return OKResponse(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class DefaultGenericViewSet(GenericViewSet):

    pass


class DefaultModelViewSet(
    DefaultCreateModelMixin,
    DefaultRetrieveModelMixin,
    DefaultUpdateModelMixin,
    # DefaultDestroyModelMixin,
    DefaultListModelMixin,
    DefaultGenericViewSet,
):
    pass


class DefaultReadOnlyModelViewSet(
    DefaultRetrieveModelMixin,
    DefaultListModelMixin,
    DefaultGenericViewSet,
):
    pass


class DefaultCteateOrReadOnlyModelViewSet(
    DefaultCreateModelMixin,
    DefaultRetrieveModelMixin,
    DefaultListModelMixin,
    DefaultGenericViewSet,
):
    pass
