# morecopy

[![Release](https://img.shields.io/pypi/v/morecopy?label=Release&color=cornflowerblue&style=flat-square)](https://pypi.org/project/morecopy/)
[![Python](https://img.shields.io/pypi/pyversions/morecopy?label=Python&color=cornflowerblue&style=flat-square)](https://pypi.org/project/morecopy/)
[![Downloads](https://img.shields.io/pypi/dm/morecopy?label=Downloads&color=cornflowerblue&style=flat-square)](https://pepy.tech/project/morecopy)
[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.5594444-cornflowerblue?style=flat-square)](https://doi.org/10.5281/zenodo.5594444)
[![Tests](https://img.shields.io/github/actions/workflow/status/astropenguin/morecopy/tests.yml?label=Tests&style=flat-square)](https://github.com/astropenguin/morecopy/actions)

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

> **Note**
> In general, there is no need to copy immutable objects, so this package may not be necessary in most cases.
> Also, some objects may not be copied even with this package:
> In CPython, for example, integers from -5 to 256 are always uncopied for optimization.

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
