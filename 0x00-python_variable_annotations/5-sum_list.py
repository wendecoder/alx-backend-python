#!/usr/bin/env python3
"""
A module that passes complex type list to a function
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    A function that retuens the sum of the elements of the
    list
    """
    sum: float = 0
    for num in input_list:
        sum = sum + num
    return sum
