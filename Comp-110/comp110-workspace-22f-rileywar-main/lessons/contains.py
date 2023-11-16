"""Example implementing a list utility function."""

# function name: contains
# we will have 2 parameters: needle (str), haystack (list[str])
# return type bool
def contains(needle: str, haystack: list[str]) -> bool:
# Gameplan:
# 1. Start with first index
    i: int = 0
# 2. loop through every index
    while i < len(haystack):
        #   2.A. Test if item at index equal to needle
        if haystack[i] == needle:
        #      2.A.True return True! We found it!
            return True
        i += 1
    return False