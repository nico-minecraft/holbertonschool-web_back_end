#!/usr/bin/env python3
"""Module that defines an asynchronous generator yielding random numbers."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Loop 10 times, asynchronously wait 1 second on each iteration, and
    yield a random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
