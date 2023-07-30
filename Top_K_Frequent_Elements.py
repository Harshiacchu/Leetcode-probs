class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}
        b = []
        if len(nums)==k:
            return nums
        for i in nums:
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1
        n = sorted(a.values(),reverse=True)[k-1]
        for i in a:
            if a[i]<n:continue
            else: b.append(i)
        return b
