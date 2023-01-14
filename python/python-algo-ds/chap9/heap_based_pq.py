"""
Heap Data Structure

A heap is a BT that stores a collection of items and satisfies two additional properties:
    1. Relational-property: Heap-Order property
        - in a heap T, for every position p other than root,
          the key stored at p is >= key stored at p's parent
        - The minimum is always stored at the root
    2. Structural-property: Complete BT property
        - A heap T with height h is complete BT if all internal levels (0, 1, 2... h - 1)
          have the max numbers of nodes possible, and at the leaf level (level h), all the nodes
          reside in the leftmost possible positions at that level

The height of a heap storing n entries is given by
    - h = floor(log n)
"""
from priority_queue_base import PriorityQueueBase


class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented PQ implemented with a binary heap"""

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    # C-9.30
    # non-recursive upheap
    def _upheap_iter(self, j):
        parent = self._parent(j)
        while parent > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            parent = self._parent(parent)

    def _downheap(self, j):
        """Determine smallest child and swap with it, recurse"""
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)

    # C-9.31
    # non-recursive downheap
    def _downheap_iter(self, j):
        current = j
        while self._has_left(current):
            left = self._left(current)
            small_child = left
            if self._has_right(current):
                right = self._right(current)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[current]:
                self._swap(current, small_child)
                current = small_child

    # ---- PUBLIC ------

    def __init__(self, contents=()):
        """
        Create a new PQ

        By default, the queue will be empty, if contents is given,
        it should be as an iterable sequence of (k,v) tuples
        specifying the initial contents
        """
        self._data = [self._Item(k, v) for k, v in contents]
        if len(self._data) > 1:
            # if contents is given, ensure they follow heap properties
            self._heapify()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        """Add a KV pair to the end of PQ and upheap"""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)

    def min(self):
        if self.is_empty():
            raise ValueError("PQ is empty")
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise ValueError("PQ is empty")
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)

    def _heapify(self):
        """Bottom up heap construction
        This runs in O(n) time, as opposed to multiple calls to add operation
        which will take O(nlogn) in the worst case
        """
        start = self._parent(len(self) - 1)  # start at parent of last leaf
        for j in range(start, -1, -1):  # going to and including the root
            self._downheap(j)

    def to_list(self):
        result = []
        while not self.is_empty():
            (_, value) = self.remove_min()
            result.append(value)
        return result

    # C-9.32
    def find_insertion_position(self):
        z = None
        if self.is_empty():
            z = self.root()
        else:
            z = self._last  # assume reference to last node exists as _last instance
            while not self.is_root(z) and z == self.right(self.parent(z)):
                # while z is the right child of its parent
                z = self.parent(z)
            if not self.is_root(z):
                # if we stop before root, move to the right child
                z = self.right(self.parent(z))
            while not self.is_leaf(z):
                # find the bottom most left child
                z = self.left(z)
        return z

    # -------------------------------------------------------------------
    # C-9.35
    def is_leaf(self, j):
        return not self._has_right(j) and not self._has_left(j)

    def find_less_than(self, k):
        result = []
        self._find_less_than(k, 0, result)
        return result

    def _find_less_than(self, k, j, acc):
        print("j: ", j)
        if self._data[j]._key < k:
            print(self._data[j]._key)
            acc.append(self._data[j]._key)
            if self._has_left(j):
                self._find_less_than(k, self._left(j), acc)
            if self._has_right(j):
                self._find_less_than(k, self._right(j), acc)

    # -------------------------------------------------------------------

    # C-9.39
    def heap_push_pop(self, e):
        """
        Push element e on the list and then pop and return smallest item

        If the newly pushed element becomes the smallest, return it immediately
        else
        the new element takes the position of the popped root and a downheap is performed
        """
        if self.is_empty():
            return e
        if e < self._data[0]._key:
            return e
        result = self._data[0]
        self._data[0] = self._Item(e, e)
        self._downheap(0)
        return result._key

    # -------------------------------------------------------------------

    # C-9.40
    def heap_replace(self, e):
        """
        Similar to heap_push_pop but equivalent to the pop being performed first
        in other words, the new element cannot be returned as the smallest
        """
        if self.is_empty():
            self.add(e, e)
            return None
        result = self._data[0]
        self._data[0] = self._Item(e, e)
        self._downheap(0)
        return result._key


if __name__ == "__main__":
    pq = HeapPriorityQueue()
    pq.add(0, "a")
    pq.add(-1, "b")
    pq.add(-2, "c")
    pq.add(3, "d")
    pq.add(4, "f")
    pq.add(5, "g")

    # print(pq.to_list())

    # print(pq.find_less_than(2))

    print("root: ", pq._data[0]._key)
    print("heappushpop: ", pq.heap_replace(4))
    print("root: ", pq._data[0]._key)
    print(pq.to_list())

# ---- Exercises ----

# R-9.2
# Ranking by pre-order traversal already satisfies the heap order property
# after that we only need heap completeness property for a BT to be called a heap

# R-9.3
# PQ
# add(5,A)      -> (5,A)
# add(4,B)      -> (4,B),(5,A)
# add(7,F)      -> (4,B),(5,A),(7,f)
# add(1,d)      -> (1,d),(4,B),(5,A),(7,f)
# remove_min    -> (4,B),(5,A),(7,f)         -> (1,d)
# add(3,j)      -> (3,j),(4,B),(5,A),(7,f)
# add(6,l)      -> (3,j),(4,B),(5,A),(6,l),(7,f)
# remove_min    -> (4,B),(5,A),(6,l),(7,f)   -> (3,j)
# remove_min    -> (5,A),(6,l),(7,f)         -> (4,B)
# add(8,G)      -> (5,A),(6,l),(7,f),(8,g)
# remove_min    -> (6,l),(7,f),(8,g)         -> (5,A)
# add(2,h)      -> (2,h),(6,l),(7,f),(8,g)
# remove_min    -> (6,l),(7,f),(8,g)         -> (2,h)
# remove_min    -> (7,f),(8,g)               -> (6,l)

# R-9.10
# At which position of a heap might the 3rd smallest key be stored?
# Has to be the right child of root

# R-9.11
# Where would the largest key be in the heap
# Any of the leaf nodes of the BT

# R-9.12
# how can a max-oriented PQ with numeric keys be implemented with a min-oriented PQ?
# Just negate the numbers and use normal PQ

# R-9.14
# let T be a complete BT with positon p stores value = its level numbering
# is it a heap?
# Answer: Yes, because each number stores either 2*parent + 1 or 2 * parent + 2
# hence more than its parent, and the tree is complete

# R-9.15
# Explain why the description of down-heap bubbling does not consider the case in which
# position p has a right child but not a left child
# because by heap completeness property it is not possible for a heap to have a right
# child but not a left child

# R-9.16
# heap H with 7 distinct keys - can any tree traversal yield a decreasing or increasing order?
# Pre-order - yes, decreasing order if the heap is min-oriented
# Post-order - yes, increasing order if the heap is max-oriented
# In-inorder - no, it is not possible

# R-9.17
# let H be a heap storing 15 entries with array based representation
# What is the sequence of indices visited in each tree traversal:
# Pre-order
# 0, 1, 3, 7, 15, 8, 4, 9, 10, 2, 5, 11, 12, 6, 13, 14
# Post-order
# 15, 7, 8, 3, 9, 10, 4, 1, 11, 5, 12, 13, 6, 14, 2, 0
# in-order
# 15, 7, 3, 8, 1, 9, 4, 10, 0, 11, 5, 12, 2, 13, 6, 14

# R.9-24
# n insertions in a heap that require Sigma(n logn)
# Design the heap such that each insertion takes log n time

# C-9.41 & C-9.42
# To select top logn items from a list of n items
# Take the n items list and construct a heap using bottom-up construction
# which is O(n)
# then call remove_min logn times to select top logn items
# each of which takes log n time, hence total time is O(logn . logn)
# which is still O(n)
