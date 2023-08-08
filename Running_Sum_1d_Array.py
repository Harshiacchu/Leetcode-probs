# Leetcode: https://leetcode.com/problems/running-sum-of-1d-array/description/
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a = []
        
        for i in range(len(nums)):
            if i==0:
                a.append(nums[i])
            if i!=0:
                a.append(nums[i]+a[i-1])
        return a
