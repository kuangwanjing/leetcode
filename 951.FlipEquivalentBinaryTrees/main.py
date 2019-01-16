# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isNodeEqual(self, node1, node2):
        return (not node1 and not node2) or (node1 and node2 and node1.val == node2.val)
    
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 is None or root2 is None: return not root1 and not root2   
        if root1.val != root2.val: return False
        
        # use the if-short-circuit to reduce the amount of calculation
        # and if the value of the two nodes are not the same, stop the recursion
        return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right) or \
                self.flipEquiv(root1.right, root2.left) and self.flipEquiv(root1.left, root2.right) 

        """
        if root1 is None or root2 is None: return not root1 and not root2
        
        if root1.val != root2.val: return False
        
        if self.isNodeEqual(root1.left, root2.left) and self.isNodeEqual(root1.right, root2.right):
            return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        elif self.isNodeEqual(root1.left, root2.right) and self.isNodeEqual(root1.right, root2.left):
            return self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        else: return False
        """
