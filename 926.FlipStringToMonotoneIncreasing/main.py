class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        def dfs(S, one_flipped):            
            last = '0'
            ans = len(S)      
            for i, cur in enumerate(S):
                if last == '1' and cur == '0':
                    # flip the following 0s to 1s
                    count = 0
                    for s in S[i:]:
                        if s == '0': count += 1
                    ans = min(ans, count)     
                    # if a step before has flipped 0s to 1s, then the 1s can't be flipped again.
                    if not one_flipped:
                        # flip the previous 1s to 0s
                        j = i - 1 
                        while j >= 0 and S[j] == '1': j -= 1
                        if i - j - 1 <= ans:
                            ans = min(ans, i - j - 1 + dfs(S[i:], one_flipped))
                    return ans
                last = cur                 
            return 0
        # call dfs        
        return dfs(S, False)


class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """

        zero,one = 0,0
        for s in S:
            if s=="0":
                zero+=1
        min_flip = zero
        for s in S:
            if s=="0":
                zero-=1
            else:
                one+=1
            min_flip = min(min_flip, zero+one)
        return min_flip
