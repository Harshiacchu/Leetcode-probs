#Leetcode: https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return sorted(nums) [-k]

        a = []

        for i in nums:
            if len(a) < k:
                heapq.heappush(a, i)
            else:
                if i > a[0]:
                    heapq.heappushpop(a, i)
        
        return heapq.heappop(a)
