# Leetcode: https://leetcode.com/problems/add-digits/description/
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # def c_sum(nums):
        #     s = sum([int(i) for i in str(nums)])
        #     if len(str(s)) == 1:
        #         return s
        #     return c_sum(s)
        # return c_sum(num)
        return mod(num, 9) or min(num, 9)
