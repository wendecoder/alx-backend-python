#!/usr/bin/env python3
"""
A module that passes a complex type list that is a mix
of integers and floats
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """A function that returns the sum of the elements of
    the list as a float
    """
    return float(sum(mxd_lst))
