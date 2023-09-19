# Leetcode: https://leetcode.com/problems/find-the-duplicate-number/description/
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = {}
        c = nums[0]
        for i in nums:
          if i in a:
            c = i
            break
          else:
            a[i] = 1
        return c
        
        
