class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.vectors = [v1, v2]
        self.ptrs = [0, 0]
        self.vp = 0
    def next(self):
        """
        :rtype: int
        """
        while True:
            if self.ptrs[self.vp] < len(self.vectors[self.vp]):
                val = self.vectors[self.vp][self.ptrs[self.vp]]
                self.ptrs[self.vp] += 1
                self.vp = (self.vp + 1) % 2
                return val
            else: self.vp = (self.vp + 1) % 2

    def hasNext(self):
        """
        :rtype: bool
        """
        return True in [ p < len(self.vectors[i]) for i, p in enumerate(self.ptrs)]

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
