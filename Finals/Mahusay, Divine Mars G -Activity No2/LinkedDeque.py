from DoublyLinkedBase import _DoublyLinkedBase
class LinkedDeque(_DoublyLinkedBase):
    '''Double ended queue implementation based on a doubly linked list.'''
    def first(self):
        '''Return but do not remove the element at the front of the deque'''
        if self.is_empty():
            raise Exception("Deque is empty!")
        return self._header._next._element
    def last(self):
        '''Return but do not remove the element at the back of the deque'''
        if self.is_empty():
            raise Exception("Deque is empty!")
        return self._trailer._prev._element
    def insert_first(self, e):
        '''Add an element to the fron of the deque.'''
        self._insert_between(e, self._header, self._header._next)
    def insert_last(self, e):
        '''Add an element to the back of the deque'''
        self._insert_between(e, self._trailer._prev, self._trailer)
    def delete_first(self):
        '''Remove and return the element from the front of the deque.'''
        '''Raise Exception if the deque is empty.'''
        if self.is_empty():
            raise Exception("Deque is empty!")
        return self._delete_node(self._header._next)
    def delete_last(self):
        '''Remove and return the element from the back of the deque.'''
        '''Raise Exception if the deque is empty.'''
        if self.is_empty():
            raise Exception("Deque is empty!")
        return self._delete_node(self._trailer._prev)
    def __str__(self):
        """Return a string representation of the deque's contents."""
        elements = []
        current = self._header._next
        while current is not self._trailer:
            elements.append(str(current._element))
            current = current._next
        return "[" + ", ".join(elements) + "]"