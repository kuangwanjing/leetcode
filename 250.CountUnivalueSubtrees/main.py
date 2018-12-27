# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def recursiveCount(self, root):
        if root == None:
            return 0, True
        if root.left == None and root.right == None:
            return 1, True
        lc, leftUnival = self.recursiveCount(root.left)
        rc, rightUnival = self.recursiveCount(root.right)
        if root.left == None:
            return (rc + 1, True) if root.right.val == root.val and rightUnival else (rc, False)
        if root.right == None:
            return (lc + 1, True) if root.left.val == root.val and leftUnival else (lc, False)
        if root.right.val == root.left.val and root.right.val == root.val and leftUnival and rightUnival:
            return (lc + rc + 1, True)
        else:
            return (lc + rc, False)
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        rst, uni = self.recursiveCount(root)
        return rst

# This solution is inspired by "https://leetcode.com/problems/count-univalue-subtrees/discuss/67602/Java-11-lines-added"
# in the above solution, the author use "|" instead of "||" to avoid the short circuit so that the right subtree is counted even though the left subtree is not univalue.
class Solution2:
    def checkUnival(self, root, val):
        if root == None:
            return True
        leftUnival = self.checkUnival(root.left, root.val)
        rightUnival = self.checkUnival(root.right, root.val)
        if not leftUnival or not rightUnival: return False
        self.count += 1
        return True if root.val == val else False
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        self.checkUnival(root, 0)
        return self.count 
