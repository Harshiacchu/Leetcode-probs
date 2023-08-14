
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Approach - 1
        # a = {}
        # for i in nums:
        #     if i in a:
        #         a[i] += 1
        #     else:
        #         a[i] = 1
        
        # for i in a.keys():
        #     if a[i] == max(a.values()):
        #         return i

    #Approach - 2
        return sorted(nums)[len(nums)//2]
