from __future__ import annotations


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    '''
    This function takes as  arguments a list of heights and weights
    and returns a list of the associated body mass indexes
    '''
    if len(height) != len(weight):
        raise AssertionError("Lists do not have the same length")
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise AssertionError("Lists should contain only int or float")
    return [w / h ** 2 for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    This functions takes as argument a list of int or float values
    and a limit value
    it returns a list of booleans telling weither the values
    are above the limit or not
    '''
    for i in bmi:
        if isinstance(i, (int, float)) is False:
            raise AssertionError("Bmi list should only contain int or floats")
        if isinstance(limit, int) is False:
            raise AssertionError("Limit value should be an integer")
    return [(i > limit) for i in bmi]
