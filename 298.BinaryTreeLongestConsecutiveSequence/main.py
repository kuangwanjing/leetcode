# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 1
        def countConsecutive(node):
            if node == None: return 0   
            left_consecutive = countConsecutive(node.left)
            right_consecutive = countConsecutive(node.right)
            # this decide whether to form a path by joining the left child or the right child:
            if node.left and node.left.val == node.val+1:
                # if the values of parent and left child are consecutive, form a path
                left_consecutive += 1
            else: left_consecutive = 1
            if node.right and node.right.val == node.val+1:
                # if the values of parent and right child are consecutive, form a path
                right_consecutive += 1
            else: right_consecutive = 1
            # choose the longest path from the two
            max_length = max(left_consecutive, right_consecutive)
            # refresh the longest record
            self.longest = max(max_length, self.longest)
            return max_length
        countConsecutive(root)
        return self.longest

class C:
    def A(self):
        text = "abb"
        def B():
            text= "bbb" # text in B is local variable in B but not the variable in A
            # refer to https://stackoverflow.com/questions/21959985/why-cant-python-increment-variable-in-closure for detailed information
            print text
        B()

if __name__ == "__main__":
    root = TreeNode(1)
    sol = Solution()
    print sol.longestConsecutive(root)

    c = C()
    c.A()
