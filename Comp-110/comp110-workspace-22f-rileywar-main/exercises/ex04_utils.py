"""EX04 List Utils."""

__author__ = str(730579921)


def all(int_list: list[int], given: int) -> bool: 
    """Checks if all ints equal given int."""
    i: int = 0
    if len(int_list) == 0:
        return False
    while i < len(int_list):
        if given == int_list[i]:
            i += 1
        else:
            return False
    return True


def max(input: list[int]) -> int: 
    """Finds the largest variable in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        i: int = 1
        max_number: int = input[0]

        while i < len(input):
            if input[i] > max_number:
                max_number = input[i]
            i += 1

        return max_number


def is_equal(list_1: list[int], list_2: list[int]) -> bool: 
    """Checks if two lists are equal."""
    i: int = 0
    if len(list_1) != len(list_2):
        return False
    while i < len(list_1):
        if list_1[i] == list_2[i]:
            i += 1
        else:
            return False
    return True
