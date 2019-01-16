class DSU(object):
    def __init__(self, n):
        self.par = range(n)
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        # union without rank
        # self.par[self.find(x)] = self.find(y)
        # union with rank to maintain the union balance in height
        self.par[self.find(x)] = self.find(y)
    
class Solution(object):
   
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """  
        N = len(stones)
        dsu = DSU(20000)
        for x, y in stones:
            dsu.union(x, 10000 + y)
        # the number of unique union is the number of stones that will be left after the removing
        return N - len({dsu.find(x) for x, y in stones})
        
        # bfs
        """
        graph = {}
        #construct a graph whose vertices are stones and each edge means
        #its endpoints have the same row or column.
        for i, s in enumerate(stones):
            x, y = s
            rk = "r_" + str(x)
            ck = "c_" + str(y)
            if not rk in graph: graph[rk] = []
            if not ck in graph: graph[ck] = []
            graph[rk].append(i)
            graph[ck].append(i)
        #traverse the graph and do the counting
        rst = 0
        visited = [False] * len(stones)
        for i in range(len(stones)):
            if visited[i]: continue
            visited[i] = True
            s = [i]
            while s:
                cur = s.pop(0)
                rst += 1
                # push the stones with the same the row or column into the stack
                for j in ["r_"+str(stones[cur][0]), "c_"+str(stones[cur][1])]:
                    for st in graph[j]:
                        if visited[st]: continue
                        visited[st] = True
                        s.append(st)
            rst -= 1 # one stone is left
        return rst
        """
                        
