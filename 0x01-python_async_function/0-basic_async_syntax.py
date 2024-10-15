#!/usr/bin/env python3
"""using asyncio with random"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """funtion returning delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
