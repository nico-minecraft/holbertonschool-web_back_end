#!/usr/bin/env python3
"""Module that runs several random-delay coroutines concurrently."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the given max_delay and return the
    list of all the delays in ascending order, which is the order in which
    the coroutines complete, so no sorting is needed.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
