# Disjoin Set of Union(Graph Theory: connected component)
# https://leetcode.com/problems/redundant-connection/solution/
class DSU(object):
    def __init__(self, n):
        self.par = range(n+1)
        self.rnk = [0] * (n+1)
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        # union without rank
        # self.par[self.find(x)] = self.find(y)
        # union with rank to maintain the union balance in height
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True
        
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = 1    
        for u, v in edges:
            n = max(n, u, v)   
        dsu = DSU(n)
        for u, v in edges:
            # if u and v is connected with some path(s) before, then adding the current edge causes the cycle
            if not dsu.union(u, v): return [u, v]
            #if dsu.find(u) == dsu.find(v): return (u, v)
            #dsu.union(u, v)
        return []
