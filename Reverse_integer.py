# Leetcode : https://leetcode.com/problems/reverse-integer/description/
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = "" if ((str(x)[0]).isdigit()) else (str(x)[0])
        # print(sign,1)
        num = int((str(x)[::-1])) if(sign=="") else int(sign+(str(x)[:-len(str(x)):-1]))
        if num > -(2**31) and num <= (2**31)-1:
            return num
        else:
            return 0
