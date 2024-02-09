import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''
    Takes as argument a list and 2 indexes
    and returns the slice of that list between those two indexes
    '''
    if not isinstance(family, list):
        raise AssertionError("family should be a list")
    if not isinstance(start, int) or not isinstance(end, int):
        raise AssertionError("both start and end should be integers")
    print(f"My shape is : {np.array(family).shape}")
    sliced = family[start:end]
    print(f"My new shape is : {np.array(sliced).shape}")
    return sliced
