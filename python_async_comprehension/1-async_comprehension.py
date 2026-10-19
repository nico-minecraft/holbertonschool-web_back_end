#!/usr/bin/env python3
"""Module that collects random numbers using an async comprehension."""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers from async_generator using an async
    comprehension and return them as a list of floats.
    """
    return [number async for number in async_generator()]
