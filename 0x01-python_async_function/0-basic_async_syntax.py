#!/usr/bin/env python3
"""
A module that uses python asyncio package
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """A function that returns the delay time"""
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
