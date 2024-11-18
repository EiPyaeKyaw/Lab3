import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    #result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_sort_ascending():
    input_arr = [1, 2, 3, 81, 5]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    test = [1, 2, 3, 5, 81]
    assert (result == test)

def test_sort_descending():
    input_arr = [1, 2, 3, 81, 5]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    test = [81, 5, 3, 2, 1]
    assert (result == test)
