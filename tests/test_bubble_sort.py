from ..sorting.bubble_sort import bubble_sort

# unit тесты
def test_unit_sort_1():
    assert bubble_sort([1,32253,3,533,5,0]) == [0, 1, 3, 5, 533, 32253]

def test_unit_sort_2():
    assert bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

# критические случаи
def test_crit_case_sort_1():
    assert bubble_sort([1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1]

def test_crit_case_sort_2():
    assert bubble_sort([0, 1, 3, 5, 533, 32253]) == [0, 1, 3, 5, 533, 32253]

def test_crit_case_sort_3():
    assert bubble_sort([1]) == [1]

def test_crit_case_sort_4():
    assert bubble_sort([]) == []
