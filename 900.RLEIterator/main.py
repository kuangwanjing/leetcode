class RLEIterator:

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.times = []
        self.numbers = []
        
        for i, a in enumerate(A):
            if i % 2 == 0:
                self.times.append(a)
            else:
                self.numbers.append(a)
    
        self.ptr = 0 if len(A) > 0 else -1

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.ptr == -1: return -1
        
        acc = 0
        
        while acc < n:
            if self.ptr == len(self.numbers):
                self.ptr = -1
                return -1
            if acc + self.times[self.ptr] < n:
                acc += self.times[self.ptr]
                self.ptr += 1
            else:
                self.times[self.ptr] -= n - acc
                acc = n    
        return self.numbers[self.ptr]

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
