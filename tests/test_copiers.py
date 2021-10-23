# standard library
from types import FunctionType, LambdaType
from typing import Type, TypeVar


# dependencies
from morecopy.copiers import copiers
from pytest import mark


# type hints
T = TypeVar("T")


# test data
def function(a: int, b: int) -> int:
    return a + b


test_header = "type_, value"
test_data = [
    (int, 1234567890),
    (float, 1.234567890),
    (complex, 1.2345 + 6.7890j),
    (str, "lorem ipsum"),
    (bytes, b"lorem ipsum"),
    (tuple, (123, 4.56, 7.8e90)),
    (range, range(1234567890)),
    (slice, slice(1234, 5678, 90)),
    (frozenset, frozenset({123, 4.56, 7.8e90})),
    (FunctionType, function),
    (LambdaType, lambda a, b: a + b),
]


# test functions
@mark.parametrize(test_header, test_data)
def test_copier_eq(type_: Type[T], value: T) -> None:
    if type_ is FunctionType:
        return

    assert value == copiers[type_](value)


@mark.parametrize(test_header, test_data)
def test_copier_is(type_: Type[T], value: T) -> None:
    assert value is not copiers[type_](value)
