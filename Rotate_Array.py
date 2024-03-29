class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = (nums[:-k%len(nums)] [::-1] + nums[-k%len(nums):] [::-1])[::-1]
