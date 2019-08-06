#https://en.wikipedia.org/wiki/Change-making_problem

# this is a bottom-to-top solution,
# leetcode also provides a top-to-bottom solution which use backtracing and caching.
from bisect import bisect_right

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        cnt = [-1 for i in range(amount+1)]
        cnt[0] = 0
        coins.sort()
        
        
        for idx in range(1, amount+1):
            max_coin_idx = bisect_right(coins, idx)
            for cindx in range(max_coin_idx):
                c = coins[cindx]
                if idx >= c and cnt[idx-c] >= 0:
                    if cnt[idx] == -1:
                        cnt[idx] = cnt[idx-c] + 1
                    else: cnt[idx] = min(cnt[idx], cnt[idx-c] + 1)
        
        return cnt[amount]
