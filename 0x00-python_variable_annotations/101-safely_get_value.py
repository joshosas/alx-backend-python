#!/usr/bin/env python3
'''Task 11's module - Type Annotations.
'''
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')
Resp = Union[Any, T]
Define = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Define = None) -> Resp:
    '''Returns a value from a dict using a given key.
    '''
    if key in dct:
        return dct[key]
    else:
        return default

