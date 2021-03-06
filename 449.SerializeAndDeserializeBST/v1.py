# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# the solution use the construction of preorder/postorder and inorder to restore a binary search tree.
# this solution aims to optimize the encoded space
# In the solution, postorder and inorder are used, my solution tries to use preorder and inorder instead.
class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def preorder(root):
            return [root.val] + preorder(root.left) + preorder(root.right) if root else []
        
        return ",".join(map(str, preorder(root)))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        
        def helper(lower = float("-inf"), upper = float("inf")):
            if not data or data[0] < lower or data[0] > upper:
                return None
            val = data.pop(0)
            root = TreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root
        
        data = [int(x) for x in data.split(",") if x]
        
        return helper()
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
