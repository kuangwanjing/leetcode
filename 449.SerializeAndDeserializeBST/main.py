# Definition for a binary tree node.
import pdb
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        
        q = [root]
        strs = [str(root.val)]
        while q:
            cur = q.pop(0)
            if cur.left is not None:
                q.append(cur.left)
                strs.append(str(cur.left.val))
            else:
                strs.append("#")
            if cur.right is not None:
                q.append(cur.right)
                strs.append(str(cur.right.val))
            else:
                strs.append("#")
        print strs
        return ",".join(strs)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        elems = data.split(",")
        if len(elems) == 0:
            return None
        q = []
        for elem in elems:
            if elem != "#":
                q.append(TreeNode(elem))
            else:
                q.append(None)
        l = len(q)
        pdb.set_trace()
        for i in range(l):
            if q[i] is not None:
                if 2*i < l:
                    q[i].left = q[2*i+1]
                if 2*i+1 < l:
                    q[i].right = q[2*i+2]
        root = q[0]
        return root 

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
# Your Codec object will be instantiated and called as such:
codec = Codec()
t = codec.deserialize(codec.serialize(root))
print codec.serialize(t)
