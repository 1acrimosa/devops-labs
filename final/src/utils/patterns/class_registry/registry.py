"""Registry pattern for classes."""

__all__ = ["ClassRegistry"]

import typing

from .base import BaseMutableRegistry, RegistryKeyError

T = typing.TypeVar("T")


class ClassRegistry(BaseMutableRegistry[T]):
    """Maintains a registry of classes and provides a generic factory for instantiating them."""

    def __init__(
        self,
        attr_name: typing.Optional[str] = None,
        unique: bool = False,
    ) -> None:
        """Construct a new class registry.

        :param attr_name:
            If provided, :py:meth:`register` will automatically detect the key to use
            when registering new classes.

        :param unique:
            Determines what happens when two classes are registered with the same key:

            - ``True``: A :py:class:`KeyError` will be raised.
            - ``False``: The second class will replace the first one.
        """
        super().__init__(attr_name)

        self.unique = unique

        self._registry: dict[typing.Hashable, typing.Type[T]] = {}

    def __repr__(self) -> str:
        """Representation."""
        return f"{type(self).__name__}(attr_name={self.attr_name!r}, unique={self.unique!r})"

    def get_class(self, key: typing.Hashable) -> typing.Type[T]:
        """Return the class associated with the specified key."""
        lookup_key = self.gen_lookup_key(key)

        try:
            return self._registry[lookup_key]
        except KeyError:
            return self.__missing__(lookup_key)

    def _register(self, key: typing.Hashable, class_: typing.Type[T]) -> None:
        """Register a class with the registry.

        :param key: Has already been processed by :py:meth:`gen_lookup_key`.
        """
        if key in ["", None]:
            raise ValueError(
                f"Attempting to register class {class_.__name__} "
                "with empty registry key {key!r}."
            )

        if self.unique and (key in self._registry):
            raise RegistryKeyError(
                f"{class_.__name__} with key {key!r} is already registered.",
            )

        self._registry[key] = class_

    def _unregister(self, key: typing.Hashable) -> typing.Type[T]:
        """Unregister the class at the specified key.

        :param key: Has already been processed by :py:meth:`gen_lookup_key`.
        """
        return self._registry.pop(key) if key in self._registry else self.__missing__(key)
