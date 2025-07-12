def test_segregation_sort():
    test_cases = [
        ([3, 1, 2], [1, 2, 3]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([7, 2, 6, 1, 8, 15], [1, 2, 6, 7, 8, 15]),
        ([9, 9, 9, 9], [9, 9, 9, 9]),
        ([], []),
        ([36], [36]),
        ([2, -5, 1, -8, 13], [-8, -5, 1, 2, 13]),
        ([15, 13, 16, 2, 5, -2], [-2, 2, 5, 13, 15, 16]),
    ]
    for i, (input_list, expected_output) in enumerate(test_cases):
        array = input_list.copy()
        SegregationSort(array, 0, len(array) - 1)
        assert array == expected_output, f"Test case {i + 1} failed: expected {expected_output}, got {array}"

        