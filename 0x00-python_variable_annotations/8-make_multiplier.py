#!/usr/bin/env python3
"""type-annotated function make_multiplier that takes a float multiplier as"""


def make_multiplier(multiplier: float) -> callable:
    """return a function that multiplies a float by multiplier"""
    def multiply(n: float) -> float:
        """return a float multiplied by multiplier"""
        return n * multiplier
    return multiply
