"""EX07 dictionaries."""

__author__ = str(730579921)


def invert(normal: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of str, returns a dictionary that inverts the keys and values."""
    inverted = {}
    dict_list: list[str] = list()
    for key in normal:
        if normal[key] in dict_list:
            raise KeyError("No duplicate keys allowed!")
        dict_list.append(normal[key])
    for key in normal:
        inv = normal[key]
        inverted[inv] = key
    return inverted

def favorite_color(name_color: dict[str, str]) -> str:
    """Given a dict of names and colors, returns the color that appears most often"""
    track: dict[str, int] = {}
    most_common: str = ""

    for value in name_color:
        if name_color[value] not in track:
            track[name_color[value]] = 1
        else:
            track[name_color[value]] += 1
    compare_num: int = 0
    for key in track:
        if track[key] > compare_num:
            compare_num = track[key]
            most_common = key
    return most_common


def count(given: list[str]) -> dict[str, int]:
    """Given a list, produces a dictionary of keys and values where the list values are the keys."""
    empty: dict[str, int] = {}
    for key in given:
        if key in empty:
            empty[key] += 1
        else:
            empty[key] = 1
    return empty
