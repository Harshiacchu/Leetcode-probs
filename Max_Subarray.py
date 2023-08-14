# Leetcode: https://leetcode.com/problems/maximum-subarray/description/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        ms = nums[0]
        cs = nums[0]

        for i in nums[1:]:
            cs = max(i, cs+i)
            ms = max(ms, cs)
        
        return ms
