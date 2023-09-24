# Leetcode: https://shorturl.at/cfFX3
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(self.cint(num1)*self.cint(num2))
    def cint(self,n):
        r = 0
        for i  in range(len(n)):
            r = r*10 + ord(n[i])-ord('0')
        return r
