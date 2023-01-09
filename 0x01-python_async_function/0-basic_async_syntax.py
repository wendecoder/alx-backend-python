#!/usr/bin/env python
# 0-basic_async_syntax.py
"""
A module that uses python asyncio package
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """A function that returns the delay time"""
    i = random.random() * max_delay
    await asyncio.sleep(i)
    return i
