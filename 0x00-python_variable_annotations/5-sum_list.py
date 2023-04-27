#!/usr/bin/env python3
'''Task 5's module - Type Annotations.
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Returns the sum of a elements in a List
    '''
    return float(sum(input_list))
