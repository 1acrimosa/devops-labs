"""Verifies registry behavior when :py:func:`class_registry.ClassRegistry.gen_lookup_key` is modified."""

import typing

import pytest

from utils.patterns.class_registry import ClassRegistry

from . import Charmander, Pokemon, Squirtle


@pytest.fixture(name="customized_registry")
def fixture_customized_registry() -> ClassRegistry[Pokemon]:
    """Fixture that returns a customized registry."""

    class CustomizedLookupRegistry(ClassRegistry[Pokemon]):
        @staticmethod
        def gen_lookup_key(key: typing.Hashable) -> typing.Hashable:
            """Generate a lookup key for the registry."""
            if isinstance(key, str):
                return "".join(reversed(key))
            return key  # pragma: no cover

    registry = CustomizedLookupRegistry()
    registry.register("fire")(Charmander)
    registry.register("water")(Squirtle)
    return registry


def test_contains(customized_registry: ClassRegistry[Pokemon]):
    """Verifies that the customized registry behaves as expected."""
    assert "fire" in customized_registry
    assert "erif" not in customized_registry


def test_getitem(customized_registry: ClassRegistry[Pokemon]):
    """Verifies that the customized registry behaves as expected."""
    assert isinstance(customized_registry["fire"], Charmander)


def test_iter(customized_registry: ClassRegistry[Pokemon]):
    """Verifies that the customized registry behaves as expected."""
    generator = iter(customized_registry)

    assert next(generator) == "fire"
    assert next(generator) == "water"

    with pytest.raises(StopIteration):
        next(generator)


def test_len(customized_registry: ClassRegistry[Pokemon]):
    """Verifies that the customized registry behaves as expected."""
    assert len(customized_registry) == 2


def test_get_class(customized_registry: ClassRegistry[Pokemon]):
    """Verifies that the customized registry behaves as expected."""
    assert customized_registry.get_class("fire") is Charmander


def test_get(customized_registry: ClassRegistry[Pokemon]):
    """Verifies that the customized registry behaves as expected."""
    assert isinstance(customized_registry.get("fire"), Charmander)


def test_unregister(customized_registry: ClassRegistry[Pokemon]):
    """Verifies that the customized registry behaves as expected."""
    customized_registry.unregister("fire")

    assert "fire" not in customized_registry
    assert "erif" not in customized_registry


def test_use_case_aliases():
    """A common use case for overriding `gen_lookup_key` is to specify some aliases (e.g., for backwards-compatibility when refactoring an existing registry)."""

    class TestRegistry(ClassRegistry[Pokemon]):
        @staticmethod
        def gen_lookup_key(key: typing.Hashable) -> typing.Hashable:
            """Simulate a scenario where we renamed the key for a class in the registry, but we want to preserve backwards-compatibility with existing code that hasn't been updated yet."""
            if key == "bird":
                return "flying"

            return key

    registry = TestRegistry()

    @registry.register("flying")
    class MissingNo(Pokemon):
        pass

    assert isinstance(registry["bird"], MissingNo)
    assert isinstance(registry["flying"], MissingNo)

    assert "bird" in registry
    assert "flying" in registry
