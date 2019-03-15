# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        # this solution depends on the feature of bst
        # every node is attached with an node interval
        # if the num is lying within the node interval, then this 
        # num is the node's child or descedant.
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stk = [(root, -1000, 1000)]
        for num in preorder[1:]:
            while stk:
                cur_node, left, right = stk[-1]
                if not left < num < right:
                    stk.pop(-1)
                    continue
                if cur_node.left == None and num < cur_node.val:
                    new_node = TreeNode(num)
                    cur_node.left = new_node
                    stk.append((new_node, left, cur_node.val))
                    break
                if cur_node.right == None and num > cur_node.val:
                    new_node = TreeNode(num)
                    cur_node.right = new_node
                    stk.append((new_node, cur_node.val, right))
                    break
        return root
