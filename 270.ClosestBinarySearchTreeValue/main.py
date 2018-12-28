import pdb
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# search the whole tree
class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        diff = abs(root.val-target)
        val = root.val
        if root.left != None:
            tmp = self.closestValue(root.left, target)
            if abs(tmp-target) < diff:
                val = tmp
                diff = abs(tmp-target)
        if root.right != None:
            tmp = self.closestValue(root.right, target)
            if abs(tmp-target) < diff:
                val = tmp
                diff = abs(tmp-target)
        print root.val, val
        return val

# search half of the tree
class Solution2:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root.left and not root.right or target == root.val: return root.val
        if target < root.val:
            if not root.left:
                return root.val
            else:
                tmp = self.closestValue(root.left, target)
                return tmp if abs(tmp-target) < abs(root.val-target) else root.val
        else:
            if not root.right:
                return root.val
            else:
                tmp = self.closestValue(root.right, target)
                return tmp if abs(tmp-target) < abs(root.val-target) else root.val

# use non-recurisve way to traverse the tree
class Solution3:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        val = root.val
        while root:
            if root.val == target: return root.val
            if abs(root.val-target) < abs(val-target):
                val = root.val
            root = root.left if target < root.val else root.right
        return val

if __name__ == "__main__":
    root = TreeNode(24)
    root.left = TreeNode(1)
    root.right = TreeNode(35)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(4)
    root.left.right.right.left = TreeNode(3)
    root.left.right.right.right = TreeNode(9)
    root.right.left = TreeNode(30)
    root.right.right = TreeNode(35)
    sol = Solution3()
    print sol.closestValue(root, 3.714286)
    print sol.closestValue(root, 3.000000)
