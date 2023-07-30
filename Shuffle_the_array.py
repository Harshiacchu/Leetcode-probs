class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a = nums[0:len(nums)//2]
        b = nums[len(nums)//2:]
        j,k = 0,0
        ans = []
        for i in range(len(nums)):
            if i%2==0:
                ans.append(a[j])
                j += 1
            else:
                ans.append(b[k])
                k += 1
        return ans
