__all__ = ["copy"]


# standard library
from copy import copy as stdlib_copy
from copy import _copy_dispatch as stdlib_copiers  # type: ignore
from threading import Lock
from typing import TypeVar


# submodules
from .copiers import copiers


# type hints
T = TypeVar("T")


# lock object
lock = Lock()


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
    with lock:
        original = stdlib_copiers.copy()

        try:
            stdlib_copiers.update(copiers)
            return stdlib_copy(obj)
        finally:
            stdlib_copiers.clear()
            stdlib_copiers.update(original)
