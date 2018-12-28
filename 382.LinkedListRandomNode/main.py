import random
import pdb
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.list = head
        self.cur = head
        
    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        rst = self.cur.val
        for i in range(20):
            rand = random.randint(0, i)
            if rand == 0: rst = self.cur.val
            self.cur = self.cur.next
            if self.cur == None: 
                self.cur = self.list
        return rst
        

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
solution = Solution(head)
for i in range(100):
    print solution.getRandom()

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
