"""EX07 dictionary tests."""

__author__ = str(730579921)

from dictionary import invert, favorite_color, count


def test_invert_edge() -> None:
    """Tests for when invert has one key and value."""
    normal: dict[str, str] = {'kris': 'jordan'}
    assert invert(normal) == {'jordan': 'kris'}


def test_invert_use() -> None:
    """Tests for when invert is normal."""
    normal: dict[str, str] = {'a': 'z', 'b' : 'y', 'c': 'x'}
    assert invert(normal) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_use_2() -> None:
    """Tests for when invert is normal."""
    normal: dict[str, str] = {'apple': 'cat'}
    assert invert(normal) == {'cat': 'apple'}


def test_color_edge() -> None:
    """Tests for when favorite_color has one key and value."""
    name_color: dict[str, str] = {"Marc": "yellow"}
    assert favorite_color(name_color) == "yellow"


def test_color_use() -> None:
    """Tests for when favorite_color is normal."""
    name_color: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(name_color) == "blue"


def test_color_use_2() -> None:
    """Tests for when favorite_color is normal."""
    name_color: dict[str, str] = {"Marc": "yellow", "Ezri": "yellow", "Kris": "blue", "Riley": "blue"}
    assert favorite_color(name_color) == "yellow"


def test_count_edge() -> None:
    """Tests for when count has one value"""
    given: list[str] = ["three"]
    assert count(given) == {"three": 1}


def test_count_use() -> None:
    """Tests for when count is normal."""
    given: list[str] = ["three", "three", "one"]
    assert count(given) == {'three': 2, 'one': 1}


def test_count_use_2() -> None:
    """Tests for when count is normal."""
    given: list[str] = ["three", "three", "one", "one"]
    assert count(given) == {'three': 2, 'one': 2}
