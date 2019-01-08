import pdb
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        def inorder(root):
            if root:
                for node in inorder(root.left):
                    yield node
                yield root
                for node in inorder(root.right):
                    yield node
        
        pdb.set_trace()
        node = None
        for n in inorder(root):
            if node is not None: 
                return n
            if n.val == p.val: 
                node = n
        return None
            
if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)

    sol = Solution()
    print sol.inorderSuccessor(root, root.left)
