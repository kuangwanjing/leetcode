# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root is None: return 0
        
        s = 0
        
        if L <= root.val <= R: s += root.val
        # cut the branch
        if L < root.val:
            s += self.rangeSumBST(root.left, L, R)
        if R > root.val:
            s += self.rangeSumBST(root.right, L, R)
        
        return s 
