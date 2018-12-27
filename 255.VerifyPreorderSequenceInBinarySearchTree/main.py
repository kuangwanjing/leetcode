import pdb
class StackNode:
    def __init__(self, val, left_bound, right_bound):
        self.val = val
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.left = False
        self.right = False
class Solution:
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if not preorder: return True
        s = [StackNode(preorder[0], -10000, 10000)]
        #pdb.set_trace()
        for num in preorder[1:]:
            while s:
                cur = s[-1]
                if cur.left_bound < num < cur.val and not cur.left:
                    s[-1].left = True
                    s.append(StackNode(num, cur.left_bound, cur.val))
                    break
                if cur.val < num < cur.right_bound and not cur.right:
                    s[-1].right = True
                    s[-1].left = True
                    s.append(StackNode(num, cur.val, cur.right_bound))
                    break
                s.pop(-1)
            if not s: return False
        return True 

if __name__ == "__main__":
    sol = Solution()
    print sol.verifyPreorder([5,2,6,1,3])
    print sol.verifyPreorder([5,2,1,3,6])
    print sol.verifyPreorder([1,2,3,4,5])
