"""Class registry pattern."""

__all__ = ["ClassRegistry", "RegistryKeyError"]

from .base import RegistryKeyError
from .registry import ClassRegistry
