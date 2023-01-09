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
