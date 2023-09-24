# Leetcode: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # if target in nums:
        #     return True
        # else:
        #     return False
        nums = sorted(nums)
        low = 0
        high = len(nums) - 1
        mid = 0
    
        while low <= high:
    
            mid = (high + low) // 2
    
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return True
    
        return False
