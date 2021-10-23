# standard library
from copy import copy as stdlib_copy
from typing import Type, TypeVar


# dependencies
from morecopy.copy import copy
from pytest import mark


# type hints
T = TypeVar("T")


# test data
test_header = "type_, value"
test_data = []


# test functions
@mark.parametrize(test_header, test_data)
def test_copy_eq(type_: Type[T], value: T) -> None:
    assert value == copy(value)
    assert value == stdlib_copy(value)


@mark.parametrize(test_header, test_data)
def test_copy_is(type_: Type[T], value: T) -> None:
    assert value is not copy(value)
    assert value is stdlib_copy(value)
