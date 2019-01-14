# https://leetcode.com/problems/peeking-iterator/discuss/193827/Python3-solution-beats-99

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
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

# decorator pattern

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peek_elem = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peek_elem is None:
            self.peek_elem = self.iterator.next()
        return self.peek_elem

    def next(self):
        """
        :rtype: int
        """
        if self.peek_elem is not None:
            rst = self.peek_elem
            self.peek_elem = None
        else:
            rst = self.iterator.next()
        return rst

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peek_elem is not None: return True
        else: return self.iterator.hasNext()


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
