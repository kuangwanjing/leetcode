class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v = []
        self.p = 0
        p1, p2 = 0, 0
        while p1 < len(v1) and p2 < len(v2):
            self.v.append(v1[p1])
            self.v.append(v2[p2])
            p1 += 1
            p2 += 1
        while p1 < len(v1):
            self.v.append(v1[p1]) 
            p1 += 1
        while p2 < len(v2):
            self.v.append(v2[p2]) 
            p2 += 1
    def next(self):
        """
        :rtype: int
        """
        val = self.v[self.p]
        self.p += 1
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.p < len(self.v)
        
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
