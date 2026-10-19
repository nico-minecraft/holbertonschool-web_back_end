#!/usr/bin/env python3
"""Module that runs several task_wait_random tasks concurrently."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times with the given max_delay and return
    the list of all the delays in ascending order, which is the order in
    which the tasks complete, so no sorting is needed.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
