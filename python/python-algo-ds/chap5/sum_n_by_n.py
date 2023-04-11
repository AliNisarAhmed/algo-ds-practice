def sum_of_arr(arr_of_arrays):
    return sum(
        [sum(arr) for arr in arr_of_arrays]
    )


print(sum_of_arr([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
