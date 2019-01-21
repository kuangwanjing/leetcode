import bisect

class TopVotedCandidate:

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        
        self.top = [-1] * len(times)  
        self.times = times
        
        votes = [0] * len(times)
        current_top = persons[0]
        votes[current_top] += 1
        self.top[0] = current_top
        
        for i, p in enumerate(persons[1:]):
            votes[p] += 1
            if votes[p] >= votes[current_top]: current_top = p
            self.top[i+1] = current_top

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        return self.top[bisect.bisect(self.times, t)-1]
    
        """
        lo, hi = 0, len(self.times)-1 # hi should be len(self.times) - 1 not len(self.times) 
        
        while lo < hi - 1: 
            mid = int((hi + lo) / 2)
            if self.times[mid] == t: 
                return self.top[mid]
            elif t > self.times[mid]: lo = mid
            else: hi = mid - 1
        if self.times[hi] <= t: # missed = here
            return self.top[hi]
        else:
            return self.top[lo]
        """
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
