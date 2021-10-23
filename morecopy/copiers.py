__all__ = ["copier_for"]


# standard library
from copy import copy
from types import FunctionType
from typing import Any, Callable, Dict, TypeVar


# type hints
T = TypeVar("T")
FT = TypeVar("FT", bound=FunctionType)
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
@copier_for(slice)
@copier_for(frozenset)
def copy_by_repr(obj: T) -> T:
    """Copy an object by its repr string."""
    return eval(repr(obj))


@copier_for(FunctionType)
def copy_function(function: FT) -> FT:
    """Copy a function object."""
    copied = type(function)(
        function.__code__,
        function.__globals__,
        function.__name__,
        function.__defaults__,
        function.__closure__,
    )

    # mutable objects are copied.
    copied.__annotations__ = copy(function.__annotations__)
    copied.__dict__ = copy(function.__dict__)
    copied.__kwdefaults__ = copy(function.__kwdefaults__)

    # immutable objects are just assigned.
    copied.__doc__ = function.__doc__
    copied.__module__ = function.__module__
    copied.__name__ = function.__name__
    copied.__qualname__ = function.__qualname__

    return copied
