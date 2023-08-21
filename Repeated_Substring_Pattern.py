class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        s_fold = "".join( (s[1:], s[:-1]) )
        
        return s in s_fold
# or #Leetcode: https://leetcode.com/problems/repeated-substring-pattern/
# class Solution(object):
#     def repeatedSubstringPattern(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         return s in (s+s)[1:-1]
