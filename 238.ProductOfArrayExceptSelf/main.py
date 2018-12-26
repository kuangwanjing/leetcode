# explanation: https://leetcode.com/problems/product-of-array-except-self/discuss/135882/A-Java-solution-with-an-explanation
# in short: rst[i] = left[i] * right[i]
# and left[i] = left[i-1] * nums[i-1], right[i] = right[i+1] * nums[i+1]
# the key to solve this problem without extra space is to reuse the result and calculate in place.
class Solution:
    def productExceptSelf1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # time complexity is O(N) and space complexity is O(N)
        left = [1]
        right = [1]
        l = len(nums)
        for i in range(1, l):
            left.append(left[-1]*nums[i-1])
            right.append(right[-1]*nums[l-i])
        right.reverse()
        rst = []
        for i in range(0, l):
            rst.append(left[i]*right[i])
        return rst
    def productExceptSelf2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # time complexity is O(N) and space complexity is O(1)
        l = len(nums)
        rst = [1] * l
        right = 1
        for i in range(1, l):
            rst[i] = rst[i-1]*nums[i-1]
        for i in range(0, l):
            rst[l-i-1] *= right
            right *= nums[l-i-1]
        return rst
