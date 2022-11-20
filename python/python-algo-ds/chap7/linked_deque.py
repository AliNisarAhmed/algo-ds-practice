from doubly_linked_base import _DoublyLinkedBase


class Empty(Exception):
    pass


class LinkedDeque(_DoublyLinkedBase):
    """Double ended queue implementation based on a doubly linked list"""

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._trailer._prev._element

    def insert_first(self, e):
        """Add an element to the front of the deque"""
        # insert after header
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """Add an element to the back of the deque"""
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """Remove and return the element from the front of the queue"""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._delete_node(self._trailer._prev)
