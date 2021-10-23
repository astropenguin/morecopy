# morecopy

[![PyPI](https://img.shields.io/pypi/v/morecopy.svg?label=PyPI&style=flat-square)](https://pypi.org/project/morecopy/)
[![Python](https://img.shields.io/pypi/pyversions/morecopy.svg?label=Python&color=yellow&style=flat-square)](https://pypi.org/project/morecopy/)
[![Test](https://img.shields.io/github/workflow/status/astropenguin/morecopy/Tests?logo=github&label=Test&style=flat-square)](https://github.com/astropenguin/morecopy/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?label=License&style=flat-square)](LICENSE)
[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.5594444-blue?style=flat-square)](https://doi.org/10.5281/zenodo.5594444)

Copy even immutable objects as much as possible

## Overview

morecopy is a Python package that enables copy of immutable objects so that a copied object is equivalent but not identical to the original:

```python
from morecopy import copy


original = 1234567890
copied = copy(original)

original == copied # -> True
original is copied # -> False
```

## Installation

```shell
$ pip install morecopy
```

## Supported immutable types

The following types are supported.
For mutable types (e.g. `list`) or unsupported immutable types (e.g. `bool`, `NoneType`), `morecopy.copy` and `morecopy.deepcopy` are equivalent to `copy.copy` and `copy.deepcopy`, respectively.

Type | `morecopy.copy` | `morecopy.deepcopy`
--- | --- | ---
`int` | yes | n/a
`float` | yes | n/a
`complex` | yes | n/a
`str` | yes | n/a
`bytes` | yes | n/a
`tuple` | yes | n/a
`range` | yes | n/a
`slice` | yes | n/a
`frozenset` | yes | n/a
`FunctionType` | yes | n/a
`LambdaType` | yes | n/a

## Custom immutable copier

Users can add a custom copy function (copier) for a type.
For example, the following code defines copy of integer by creating a copy function and registering it by the `copier_for` decorator.

```python
from morecopy import copier_for


@copier_for(int)
def copy_int(integer: int) -> int:
    return eval(repr(integer))
```
