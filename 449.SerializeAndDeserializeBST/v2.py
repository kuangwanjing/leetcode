# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def int_to_str(self, val):
        bytes = [chr(val >> (i * 8) & 0xff) for i in range(4)]
        bytes.reverse()
        bytes_str = ''.join(bytes)
        return bytes_str
    
    def str_to_int(self, bytes_str):
        result = 0
        for ch in bytes_str:
            result = result * 256 + ord(ch)
        return result
    
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def preorder(root):
            return [root.val] + preorder(root.left) + preorder(root.right) if root else []
        lst = preorder(root)
        lst = [self.int_to_str(x) for x in lst]
        return 'ç'.join(lst)

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
        
        data = [self.str_to_int(x) for x in data.split('ç') if x] 
        return helper()
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
