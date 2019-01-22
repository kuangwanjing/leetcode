import pdb

#sliding window!
class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        
        ans = 0
        n = len(tree)
        i = 0
        
        while True:
            count = 1
            cur, other = tree[i], -1
            cur_ptr, other_ptr = i, -1
            for j in range(i+1, n):
                if tree[j] != tree[i]:
                    if other == -1: other = tree[j]
                    elif other != tree[j]: break
                    other_ptr = j
                else: cur_ptr = j
                count += 1
            ans = max(ans, count)
            if other_ptr != -1:
                i = max(cur_ptr, other_ptr)
                while i-1 >= 0 and tree[i-1] == tree[i]: i -= 1
            else: break   
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.totalFruit([0,1,2,2])
    print sol.totalFruit([0])
