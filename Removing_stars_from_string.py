# Leetcode: https://leetcode.com/problems/removing-stars-from-a-string/
class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = []
        for i in s:
            if i != '*':
                r.append(i)
            else:
                r.pop()
        return "".join(r)
