#Leetcode : https://leetcode.com/problems/valid-palindrome/description/
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                s1+=str(i)
        if s1.lower() == s1[-1::-1].lower():
            return True
        return False
