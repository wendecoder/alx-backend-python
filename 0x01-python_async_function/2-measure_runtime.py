#!/usr/bin/env python3
"""A module that measure the runtime for asynchroneous
function
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """A functio that returns elapsed time by a wait_n
    function
    """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - s
    return total_time / n
