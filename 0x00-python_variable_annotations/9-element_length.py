#!/usr/bin/env python3
"""
A module that uses duck type an iterable object
"""


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """A function that returns the element and length of the element of the
    iterable
    """
    return [(i, len(i)) for i in lst]
