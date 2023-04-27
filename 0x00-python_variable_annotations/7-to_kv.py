#!/usr/bin/env python3
'''Task 7's module - Type Annotations.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Returns mixed elements of string and
    integer in a Tuple
    '''
    return (k, float(v**2))
