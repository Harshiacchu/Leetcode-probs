# Leetcode: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for i in nums:
            if k<2 or i != nums[k-2]:
                nums[k] = i
                
                k += 1
        
        return k
