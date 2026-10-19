#!/usr/bin/env python3
"""Module that measures the runtime of parallel async comprehensions."""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run async_comprehension four times in parallel with asyncio.gather
    and return the total runtime in seconds.
    """
    start: float = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - start
