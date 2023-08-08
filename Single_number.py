# Leetcode: https://leetcode.com/problems/single-number/description/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = {}
        for i in nums:
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1
        for i in a.keys():
            if a[i] == 1:
                return i
