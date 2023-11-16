"""EX05 'list' utilities."""

__author__ = str(730579921)

# Name: only_evens
# Arguments: A list of integers.


def only_evens(full_list: list[int]) -> list():  
    """Given a list of ints returns only even ints."""
    evens: list[int] = []
    i: int = 0
    while i < len(full_list):
        if full_list[i] % 2 == 0:
            evens.append(full_list[i])
        i += 1
    return evens

# returns: A list of integers, containing only the even elements of the input parameter.

# Name: concat
# Parameters: Two lists of ints.


def concat(list_1: list[int], list_2: list[int]) -> list[int]:   
    """Given two lists, returns the first list followed by the second list."""
    return list_1 + list_2
# Returns: A list containing all elements of the first list, followed by all elements of the second list.

# Name: sub
# Parameters: A list and two ints, where the first int serves as a start index and the second int serves as an end index (not inclusive).


def sub(a_list: list[int], start: int, end: int) -> list[int]:  
    """Given a list and two ints, resulting list should be between start and end."""
    between: list[int] = []
    if start < 0:
        start = 0
    if end > len(a_list):
        end = len(a_list)
    if len(a_list) == 0 or start > len(a_list) or end <= 0:
        return between
    while start < end:
        between.append(a_list[start])
        start += 1
    return between
# Returns: A List which is a subset of the given list, between the specified start index and the end index - 1.