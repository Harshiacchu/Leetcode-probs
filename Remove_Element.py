#Leetcode: https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i1 = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i1] = nums[i]
                i1 += 1
        return i1
