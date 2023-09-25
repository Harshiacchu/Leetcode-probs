# Leetcode: https://leetcode.com/problems/find-the-difference/
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for i in t:
            if i not in t or t.count(i)!=s.count(i):
                return i
        
        
