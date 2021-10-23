__all__ = ["copier_for"]


# standard library
from typing import Any, Callable, Dict, TypeVar


# type hints
T = TypeVar("T")
Copier = Callable[[T], T]


# package copiers
copiers: Dict[Any, Copier[Any]] = {}


def copier_for(type_: Any) -> Callable[[Copier[T]], Copier[T]]:
    """Register a copier as one of the package copiers."""

    def register(copier: Copier[T]) -> Copier[T]:
        copiers[type_] = copier
        return copier

    return register
