#!/usr/bin/env python3
"""Module with a basic asynchronous coroutine waiting for a random delay."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random float delay between 0 and max_delay seconds
    (both included) and return the value of that delay.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
