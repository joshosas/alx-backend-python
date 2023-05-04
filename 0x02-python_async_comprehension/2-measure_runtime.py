#!/usr/bin/env python3
'''File for Task 2.
'''
import asyncio
import time
from importlib import import_module


async_comprehension = import_module('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''execute async_comprehension four times in parallel,
       measure the total runtime and returns it.
    '''
    starting_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - starting_time
