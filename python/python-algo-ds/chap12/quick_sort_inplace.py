def quick_sort_inplace(S, a, b):
    """Sort the list fro S[a] to S[b] inclusive"""

    if a >= b:
        return

    pivot = S[b]
    left = a
    right = b - 1

    while left <= right:
        # scan until reaching value >= pivot (or right marker)
        while left <= right and S[left] < pivot:
            left += 1

        # scan until reaching value <= pivot (or left marker)
        while left <= right and S[right] > pivot:
            right -= 1

        if left <= right:
            # scans did not strictly cross
            S[left], S[right] = S[right], S[left]  # swap values
            left, right = left + 1, right + 1  # shrink range

    # put pivot into its final place (currently marked by left index)
    S[left], S[b] = S[b], S[left]

    # make recursive calls
    quick_sort_inplace(S, a, left - 1)
    quick_sort_inplace(S, left + 1, b)
