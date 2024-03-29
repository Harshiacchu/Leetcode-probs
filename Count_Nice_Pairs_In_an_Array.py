class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
            MOD = 10 ** 9 + 7
            num_diff = [i - int(str(i)[::-1]) for i in nums]  # nums[i] - rev(nums[i])

            res = 0
            for i in Counter(num_diff).values(): #counter counts the no of pairs of diff
                res += i * (i -1) // 2                # nC2 as we need no of pairs 

            return res % MOD
