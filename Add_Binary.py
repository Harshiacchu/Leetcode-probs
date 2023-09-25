# Leetcode: https://leetcode.com/problems/add-binary/description/
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # c = 0 
        # s = ''
        # a = list(a)
        # b = list(b)

        # while a or b or c:
        #     if a:
        #         c += int(a.pop())
        #     if b:
        #         c += int(b.pop())
        #     s += str(c%2)
        #     c //= 2
        
        # return s[::-1]
        # c = int(a,2)+int(b,2)
        return bin(int(a,2)+int(b,2))[2:]
