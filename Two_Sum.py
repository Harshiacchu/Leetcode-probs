class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val = {}
        for i in range(len(nums)):
            if (target-nums[i]) in val:
                return [val[target-nums[i]],i]
            else:
                val[nums[i]] = i
