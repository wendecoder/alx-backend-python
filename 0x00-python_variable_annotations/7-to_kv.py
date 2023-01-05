#!/usr/bin/env python3
"""
A module that passes a string and int or float
"""


from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """A function that returns a tuple of string and float"""
    return (k, float(v**2))
