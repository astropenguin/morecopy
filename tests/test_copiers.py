# standard library
from typing import Type, TypeVar


# dependencies
from morecopy.copiers import copiers
from pytest import mark


# type hints
T = TypeVar("T")


# test data
test_header = "type_, value"
test_data = [
    (int, 1234567890),
    (float, 1.234567890),
    (complex, 1.2345 + 6.7890j),
]


# test functions
@mark.parametrize(test_header, test_data)
def test_copier_eq(type_: Type[T], value: T) -> None:
    assert value == copiers[type_](value)


@mark.parametrize(test_header, test_data)
def test_copier_is(type_: Type[T], value: T) -> None:
    assert value is not copiers[type_](value)
