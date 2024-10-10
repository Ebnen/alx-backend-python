#!/usr/bin/env python3
""" function element_length that takes a list l of strings as argument """
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """return a list of tuples"""
    return [(i, len(i)) for i in lst]
