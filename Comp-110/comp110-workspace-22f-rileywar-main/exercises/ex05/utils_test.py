"""EX05 'list' utility tests."""

__author__ = str(730579921)

from utils import only_evens, sub, concat


def test_only_edge() -> None:  
    """Tests for when only_evens is empty."""
    full_list: list[int] = []
    assert only_evens(full_list) == []


def test_only_use() -> None:  
    """Tests for use of only_evens."""
    full_list: list[int] = [1, 2, 3]
    assert only_evens(full_list) == [2]


def test_only_use_2() -> None:  
    """Tests for use of only_evens."""
    full_list: list[int] = [2, 4, 6]
    assert only_evens(full_list) == [2, 4, 6]


def test_concat_edge() -> None:  
    """Tests for when concat is empty."""
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []


def test_concat_use() -> None:  
    """Tests for use of concat."""
    list_1: list[int] = [2]
    list_2: list[int] = [2]
    assert concat(list_1, list_2) == [2, 2]


def test_concat_use_2() -> None:  
    """Tests for use of concat."""
    list_1: list[int] = [2, 4]
    list_2: list[int] = [2, 4]
    assert concat(list_1, list_2) == [2, 4, 2, 4]


def test_sub_edge() -> None:  
    """Tests for when sub should return empty."""
    a_list: list[int] = []
    assert sub(a_list, 2, 4) == []


def test_sub_use() -> None:  
    """Tests for use of sub."""
    a_list: list[int] = [10, 20, 30, 40]
    start: int = 1
    end: int = 4
    assert sub(a_list, start, end) == [20, 30, 40]


def test_sub_use_2() -> None:  
    """Tests for use of sub."""
    a_list: list[int] = [10, 20, 30, 40, 50, 60]
    start: int = 0
    end: int = 5
    assert sub(a_list, start, end) == [10, 20, 30, 40, 50]