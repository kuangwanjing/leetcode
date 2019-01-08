import copy
import pdb

class Solution1(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        rst, factors = [], []
        last_factor, remain = 1, n
        flag = False

        def findFactor(start, end):
            for i in range(start, end+1):
                if remain % i == 0: return i
            return 1

        #pdb.set_trace()
        while True:
            if not factors or flag:
                start, end = last_factor+1, remain
            else:
                start, end = last_factor, remain
            flag = False
            factor = findFactor(start, end)
            if factor in [1, n]:
                if not factors: break
                last_factor = factors.pop(-1)
                remain *= last_factor
                flag = True
            else:
                remain /= factor
                last_factor = factor
                factors.append(factor)
                if remain == 1:
                    rst.append(copy.copy(factors))
                    last_factor = factors.pop(-1)
                    flag = True
                    remain *= factor
        return rst

import math
class Solution(object):
    def getFactors(self, n):
        if n == 1: return []

        rst = []
        def dfs(factors, nfactor, remain):
            if len(factors) > 0: # if n % i == 0, then [i, n//i] is one of the answers.
                rst.append(factors+[remain])
            for i in range(nfactor, int(math.sqrt(remain))+1):
                if remain % i == 0:
                    dfs(factors+[i], i, remain//i)
        dfs([], 2, n)
        return rst
            
if __name__ == "__main__":
    sol = Solution()
    print sol.getFactors(12)
    print sol.getFactors(24)
    print sol.getFactors(1)
    print sol.getFactors(23848713)
