#!/usr/bin/env python3
"""A module that calls asyncio.run"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """A function that runs wait_random n times"""
    randomList = await asyncio.gather(
        *list(map(lambda x: wait_random(max_delay), range(n)))
    )
    task_wait_random(max_delay)
    return sorted(randomList)
