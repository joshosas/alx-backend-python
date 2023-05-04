#!/usr/bin/env python3
'''File for Task 0.
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''function yields a sequence of 10 numbers
       between 0 and 10 .
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
