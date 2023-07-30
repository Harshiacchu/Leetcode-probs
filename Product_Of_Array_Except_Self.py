class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = 0
        p = 1
        a = []
        for i in range(len(nums)):
            if nums[i]!=0:
                p *= nums[i]
            else:
                m += 1
        for i in range(len(nums)):
            if nums[i]==0 and m==1:
                a.append(p)
            elif m>=1 and nums[i]!=0:
                a.append(0)
            elif nums[i]==0 and m>=1:
                a.append(0)
            else:
                a.append(p//nums[i])
        return a
