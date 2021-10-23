__all__ = ["copier_for"]


# standard library
from typing import Any, Callable, Dict, TypeVar


# type hints
T = TypeVar("T")
Copier = Callable[[T], T]


# decorator
def copier_for(type_: Any) -> Callable[[Copier[T]], Copier[T]]:
    """Register a copier as one of the builtin copiers."""

    def register(copier: Copier[T]) -> Copier[T]:
        copiers[type_] = copier
        return copier

    return register


# builtin copiers
copiers: Dict[Any, Copier[Any]] = {}


@copier_for(int)
@copier_for(float)
@copier_for(complex)
@copier_for(str)
@copier_for(bytes)
@copier_for(tuple)
@copier_for(range)
def copy_by_repr(obj: T) -> T:
    """Copy an object by its repr string."""
    return eval(repr(obj))
