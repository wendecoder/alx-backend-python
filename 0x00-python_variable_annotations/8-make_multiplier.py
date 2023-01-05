#!/usr/bin/env python3
"""
A module that uses callable
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A function that returns a function that multiplies a float
    with the argument passed to it
    """
    return lambda y: y * multiplier
