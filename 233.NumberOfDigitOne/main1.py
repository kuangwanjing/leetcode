import pdb
# https://leetcode.com/problems/number-of-digit-one/solution/
class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        # brute force
        """
        count = 0
        for i in range(n+1):
            i_str = str(i)
            for c in i_str:
                if c == "1": count += 1
        return count
        """
        count = 0
        p = 1
        np = p * 10
        while (n >= p):
            if p == 1:
                count += n / 10 + (1 if n % 10 != 0 else 0)
            else:
                count += n / np * p  + min(max(n % np - p + 1, 0), p)
            p = np
            np *= 10
        return count
        

if __name__ == "__main__":
    sol = Solution()
    print sol.countDigitOne(110)
    print sol.countDigitOne(1)
    print sol.countDigitOne(13)
    #print sol.countDigitOne(10)
    #print sol.countDigitOne(99)
    #print sol.countDigitOne(100)
    #print sol.countDigitOne(1000)
