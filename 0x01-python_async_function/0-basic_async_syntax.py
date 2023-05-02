#!/usr/bin/env python3
'''File for Task 0.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''function waits for a random
       number of seconds and returns the wait time.
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
