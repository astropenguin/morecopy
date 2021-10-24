__all__ = ["copy"]


# standard library
from copy import copy as stdlib_copy
from copy import _copy_dispatch as stdlib_copiers  # type: ignore
from typing import Any, TypeVar


# submodules
from .copiers import copiers


# type hints
T = TypeVar("T")


# copy function
def copy(obj: T) -> T:
    """Copy an object.

    Unlike ``copy.copy``, this function even copies an immutable object
    as a different one if a dedicated copier is defined in the package.
    Otherwise, it is equivalent to ``copy.copy``.

    Args:
        obj: An object to be copied.

    Returns:
        An object copied from the original.

    """
    original = stdlib_copiers.copy()

    try:
        stdlib_copiers.update(copiers)
        return stdlib_copy(obj)
    finally:
        stdlib_copiers.clear()
        stdlib_copiers.update(original)


def send_copier(key: Any) -> None:
    """Send a builtin copier to the stdlib copiers."""
    stdlib_copiers[key] = copiers.pop(key)


def recv_copier(key: Any) -> None:
    """Receive a builtin copier from the stdlib copiers."""
    copiers[key] = stdlib_copiers.pop(key)


def swap_copiers(key: Any) -> None:
    """Swap copiers in the builtin and stdlib copiers."""
    copiers[key], stdlib_copiers[key] = stdlib_copiers[key], copiers[key]
