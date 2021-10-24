__all__ = ["copier_for"]


# standard library
from copy import copy
from types import FunctionType
from typing import Any, Callable, Dict, Iterable, TypeVar


# type hints
T = TypeVar("T")
FT = TypeVar("FT", bound=FunctionType)
IT = TypeVar("IT", bound=Iterable)
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
@copier_for(range)
@copier_for(slice)
def copy_by_repr(obj: T) -> T:
    """Copy an object by evaluating its repr string."""
    return eval(repr(obj))


@copier_for(tuple)
@copier_for(frozenset)
def copy_by_type(obj: IT) -> IT:
    """Copy an object by recreating an object of its type."""
    return type(obj)(item for item in obj)  # type: ignore


@copier_for(FunctionType)
def copy_function(obj: FT) -> FT:
    """Copy a function object by recreating it."""
    copied = type(obj)(
        obj.__code__,
        obj.__globals__,
        obj.__name__,
        obj.__defaults__,
        obj.__closure__,
    )

    # mutable objects are copied.
    copied.__annotations__ = copy(obj.__annotations__)
    copied.__dict__ = copy(obj.__dict__)
    copied.__kwdefaults__ = copy(obj.__kwdefaults__)

    # immutable objects are just assigned.
    copied.__doc__ = obj.__doc__
    copied.__module__ = obj.__module__
    copied.__name__ = obj.__name__
    copied.__qualname__ = obj.__qualname__

    return copied
