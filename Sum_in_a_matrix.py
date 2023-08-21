#Leetcode: https://leetcode.com/problems/sum-in-a-matrix/

class Solution(object):
    def matrixSum(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        l = len(nums[0])
        s = 0
        while (len(nums) and l>0):
            l1 = []
            for i in range(len(nums)):
                m = max(nums[i])
                l1.append(m)
                nums[i].remove(m)
            s += max(l1)
            l -= 1
        return s
            
