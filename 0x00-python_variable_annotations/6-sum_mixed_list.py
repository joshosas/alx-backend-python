#!/usr/bin/env python3
'''Task 6's module - Type Annotations.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Returns the sum of a mixed elements
    in a List as a float
    '''
    return float(sum(mxd_lst))
