#!/usr/bin/env python3
"""Write a type-annotated function sum_list which takes a list inp"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return sum of list of floats"""
    return sum(input_list)
