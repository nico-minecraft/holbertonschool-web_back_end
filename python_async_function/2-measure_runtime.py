#!/usr/bin/env python3
"""Module that measures the average runtime of concurrent coroutines."""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total time taken by wait_n(n, max_delay) and return the
    average time per coroutine, which is the total time divided by n.
    """
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time: float = time.time() - start
    return total_time / n
