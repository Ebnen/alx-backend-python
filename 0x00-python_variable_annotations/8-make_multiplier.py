#!/usr/bin/env python3
"""type-annotated function make_multiplier that takes a float multiplier as"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a function that multiplies a float by multiplier"""
    def multiply(n: float) -> float:
        """return a float multiplied by multiplier"""
        return n * multiplier
    return multiply
