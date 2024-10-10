#!/usr/bin/env python3
""" function element_length that takes a list l of strings as argument """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return a list of tuples"""
    return [(i, len(i)) for i in lst]
