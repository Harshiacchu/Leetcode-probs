# Leetcode: https://leetcode.com/problems/reverse-words-in-a-string/description/
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # l = s.split()
        return " ".join(s.split()[::-1])
