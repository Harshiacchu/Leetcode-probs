# Leetcode: https://leetcode.com/problems/break-a-palindrome/
class Solution(object):
    def breakPalindrome(self, p):
        """
        :type palindrome: str
        :rtype: str
        """
        if len(p)==1:
            return ""
        for i in range(len(p)//2):
            if p[i] != 'a':
                return p[:i]+'a'+p[i+1:]
        return p[:-1]+'b'
