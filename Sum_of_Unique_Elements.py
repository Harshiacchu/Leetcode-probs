# Leetcode: https://leetcode.com/problems/sum-of-unique-elements/
class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # s = 0
        # for i in nums:
        #     if nums.count(i) == 1:
        #         s += i
        return sum([(i) for i in nums if(nums.count(i)==1)])
