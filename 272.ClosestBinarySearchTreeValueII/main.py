import pdb
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def setParent(self, root, par):
        self.parents[root.val] = par
        if root.left != None: self.setParent(root.left, root)
        if root.right != None: self.setParent(root.right, root)
    def getPredecessor(self, node):
        if node.left != None:
            if node.left.right == None: return node.left
            rst = node.left.right
            while rst.right != None: rst = rst.right
            return rst
        else:
            parent = self.parents[node.val]
            while parent and parent.right != node:
                node = parent
                parent = self.parents[parent.val]
            return parent
    def getSuccessor(self, node):
        if node.right != None:
            if node.right.left == None: return node.right
            rst = node.right.left
            while rst.left != None: rst = rst.left
            return rst
        else:
            parent = self.parents[node.val]
            while parent and parent.left != node:
                node = parent
                parent = self.parents[parent.val]
            return parent
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """ 
        if k == 0: return []
        rst = []
        # find the closest node first
        val = root.val
        t = root
        node = root
        while t:
            if abs(t.val-target) < abs(val-target):
                val = t.val
                node = t
            if t.val == target: break
            t = t.left if target < t.val else t.right
        rst.append(val)
        # set parent node
        self.parents = {}
        self.setParent(root, None)
        # get the closer nodes by searching for the predecessors and sucessors
        left = node
        right = node
        pdb.set_trace()
        while len(rst) < k and (left or right):
            ln = self.getPredecessor(left) if left else None
            rn = self.getSuccessor(right) if right else None
            if len(rst) + 2 <= k:
                if ln: rst.append(ln.val)
                if rn: rst.append(rn.val)
            else:
                if ln and rn:
                    if abs(ln.val-target) < abs(rn.val-target):
                        rst.append(ln.val)
                    else:
                        rst.append(ln.val)
                else:
                    if ln: rst.append(ln.val)
                    if rn: rst.append(rn.val)
                break
            left = ln
            right = rn
        return rst

class Solution2:
    def inorder(self, root):
        if not root: return 
        for val in self.inorder(root.left):
            yield val
        yield root.val
        for val in self.inorder(root.right):
            yield val
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """ 
        if k == 0: return []
        rst = []
        for n in self.inorder(root):
            if len(rst) < k:
                rst.append(n)
            else:
                if abs(n-target) < abs(rst[0]-target):
                    rst.pop(0)
                    rst.append(n)
        return rst

# another way using heap is here: https://leetcode.com/problems/closest-binary-search-tree-value-ii/discuss/70556/Simple-DFS-%2B-Priority-Queue-Python-Solution

if __name__ == "__main__":
    sol = Solution2()
    root = TreeNode(2)
    root.left  = TreeNode(1)
    root.right = TreeNode(3)
    print sol.closestKValues(root, 5.5777, 2)
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(5)
    sol = Solution()
    print sol.closestKValues(root, 3.7223, 5)

    '''
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
    '''
