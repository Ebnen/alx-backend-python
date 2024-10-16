#!/usr/bin/env python3
""" that takes a string k and an int OR float v as arguments and returns"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return a tuple"""
    return (k, float(v**2))
