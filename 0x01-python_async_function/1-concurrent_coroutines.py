#!/usr/bin/env python3
"""
A module that uses python library package
asyncio
"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """A function that runs wait_random n times"""
    randomList = await asyncio.gather(
        *list(map(lambda x: wait_random(max_delay), range(n)))
    )
    return sorted(randomList)
