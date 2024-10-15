#!/usr/bin/env python3

""" coroutine called async_generator that takes"""
import asyncio
import random
import Generator


async def async_generator() -> Generator[float, None, None]:
    """yield a random number between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
