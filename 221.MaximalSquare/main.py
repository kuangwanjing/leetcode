#solution: https://leetcode.com/articles/maximal-square/
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        """
        # dp solution with 2D matrix
        rows = len(matrix)
        
        if rows == 0: return 0
        
        cols = len(matrix[0])
        
        dp = [[0] * (cols+1) for i in range(rows+1)]
        
        rst = 0
        
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    rst = max(rst, dp[i][j])
        
        return rst * rst
        
        """
        
        #dp solution with 1D matrix
        rows = len(matrix)
        
        if rows == 0: return 0
        
        cols = len(matrix[0])
        
        dp = [0] * (cols + 1)
        
        rst = 0
        
        for i in range(1, rows+1):
            prev = 0
            for j in range(1, cols + 1):
                tmp = dp[j]
                if matrix[i-1][j-1] == "1":
                    dp[j] = min(dp[j-1], dp[j], prev) + 1
                    rst = max(rst, dp[j])
                else:
                    dp[j] = 0
                prev = tmp
        
        return rst * rst
