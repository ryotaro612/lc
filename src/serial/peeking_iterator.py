# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        a"""
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.value = None
        if self.iterator.hasNext():
            self.value = self.iterator.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.value
        

    def next(self):
        """
        :rtype: int
        """
        result = self.value
        if self.iterator.hasNext():
            self.value = self.iterator.next()
        else:
            self.value = None
        return result
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.value is not None
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
