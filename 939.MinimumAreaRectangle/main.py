import collections
import pdb

class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        columns = collections.defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        lastx = {}
        ans = float('inf')
        
        pdb.set_trace()
        # from left to right
        for x in sorted(columns):
            column = columns[x]
            # from bottom to top
            column.sort()
            for i, y1 in enumerate(column):
                for j in range(i):
                    y2 = column[j]
                    if (y2, y1) in lastx:
                        ans = min(ans, (x - lastx[y2, y1]) * (y1 - y2))
                    lastx[y2, y1] = x
        return ans if ans < float('inf') else 0 

if __name__ == "__main__":
    sol = Solution()
    print (sol.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))
