from heap_based_pq import HeapPriorityQueue
from positional_list import PositionalList
import sys

sys.path.append("../chap7")


def pq_sort(C: PositionalList):
    """Sort a positional list using a PQ

    The runtime of this sorting algo depends on the underlying implementation of the PQ
    - as the runtime depends on `add` and `remove_min` PQ operations.

    1. If we implement PQ with an unsorted list:
        - Phase 1 takes O(n) time
        - In Phase 2 the runtime of remove_min operation is proportional to size of PQ
        - Thus the bottleneck is the repeated selection of the minimum value
        - Hence this algo is better known as Selection Sort
        - The total runtime is O(n^2)
            - as repeated remove_min is O(n + (n-1) + (n-2)...) = O(n^2)
    2. If we use a sorted list for PQ
        - then Phase 2 takes O(n)
        - but now Phase 1 becomes the bottleneck, since in the worst case each add operation takes
          time proportional to the current size of P
        - This algo now becomes Insertion sort
        - But is still O(n^2) - `add` which is O(n) runs n times
        - However, it has a best case running time of O(n), unlike selection sort
    3. If we use a Heap for PQ
        - All methods in PQ run in O(logn) time
        - Therefore, phase 1 now takes O(nlogn)
            - could be improved to O(n) with the bottom up construction technique
        - Phase 2 takes O(nlogn) time
        - This sorting algo is called Heap Sort
        - To sort the list in ascending order - use Max-oriented heap
    """
    n = len(C)
    P = HeapPriorityQueue()

    # Phase 1
    for j in range(n):
        element = C.delete(C.first())
        P.add(element, element)

    # Phase 2
    for j in range(n):
        (k, v) = P.remove_min()
        C.add_last(v)


# R-9.7 Selection sort - find min and swap with current index
# 22 15 36 44 10 3 9 13 29 25
# 3 15 36 44 10 22 9 13 29 25
# 3 9 36 44 10 22 15 13 29 25
# 3 9 10 44 36 22 15 13 29 25
# 3 9 10 13 36 22 15 44 29 25
# 3 9 10 13 15 22 36 44 29 25
# 3 9 10 13 15 22 36 44 29 25
# 3 9 10 13 15 22 25 44 29 36
# 3 9 10 13 15 22 25 29 44 36

# R-9.8 Insertion sort - for each index bring it to proper position
# 22 15 36 44 10 3 9 13 29 25
# 15 22 36 44 10 3 9 13 29 25
# 15 22 36 44 10 3 9 13 29 25
# 10 15 22 36 44 3 9 13 29 25
# 3 10 15 22 36 44 9 13 29 25
# 3 9 10 15 22 36 44 13 29 25
# 3 9 10 13 15 22 36 44 29 25
# 3 9 10 13 15 22 29 36 44 25
# 3 9 10 13 15 22 25 29 36 44

# R-9.9 Worst case scenario for Insertion sort
# Occurs when the array is in descending order
# Insertion sort then turns into O(n^2)

# R-9.13
# In place heap sort
# 2, 5, 16, 4, 10, 23, 39, 18, 26, 15
# -2, -5, -16, -4, -10, -23, -39, -18, -26, -15
# Phase 1
# -2, -5, -16, -4, -10, -23, -39, -18, -26, -15
# -5, -2, -16, -4, -10, -23, -39, -18, -26, -15
# -16, -5, -2, -4, -10, -23, -39, -18, -26, -15
# -16, -10, -2, -4, -5, -23, -39, -18, -26, -15
# -23, -10, -16, -4, -5, -2, -39, -18, -26, -15
# -39, -10, -23, -4, -5, -2, -16, -18, -26, -15
# -39, -10, -23, -18, -5, -2, -16, -4, -26, -15
# -39, -26, -23, -18, -5, -2, -16, -4, -10, -15
# -39, -26, -23, -18, -15, -2, -16, -4, -10, -5
# Phase 2
# -5, -26, -23, -18, -15, -2, -16, -4, -10, -39
# -26, -18, -23, -10, -15, -2, -16, -4, -5, -39
# -5, -18, -23, -10, -15, -2, -16, -4, -26, -39
# -23, -18, -16, -10, -15, -2, -5, -4, -26, -39
# -4, -18, -16, -10, -15, -2, -5, -23, -26, -39
# -18, -15, -16, -10, -4, -2, -5, -23, -26, -39
# -5, -15, -16, -10, -4, -2, -18, -23, -26, -39
# -16, -15, -5, -10, -4, -2, -18, -23, -26, -39
# -2, -15, -5, -10, -4, -16, -18, -23, -26, -39
# -15, -10, -5, -2, -4, -16, -18, -23, -26, -39
# -4, -10, -5, -2, -15, -16, -18, -23, -26, -39
# -10, -4, -5, -2, -15, -16, -18, -23, -26, -39
# -2, -4, -5, -10, -15, -16, -18, -23, -26, -39
# -5, -4, -2, -10, -15, -16, -18, -23, -26, -39
# -2, -4, -5, -10, -15, -16, -18, -23, -26, -39
# -4, -2, -5, -10, -15, -16, -18, -23, -26, -39
# -2, -4, -5, -10, -15, -16, -18, -23, -26, -39
# Reverse signs
# 2, 4, 5, 10, 15, 16, 18, 23, 26, 39
