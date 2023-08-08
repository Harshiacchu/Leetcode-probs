from sortedcontainers import SortedSet
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = SortedSet(nums) 
         
        m, c = 0, 0
        for num in nums:
            if num - 1 in nums:
                c += 1
            else:
                m = max(m, c)
                c = 1
        m = max(m, c)
        return m
