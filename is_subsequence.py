# Leetcode: https://shorturl.at/kxAKW
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) < 1:
            return True
        s1 = ""
        c = s[0]
        j = 0
        for i in t:
            if i == c:
                s1 += i
                if j < len(s)-1:
                    j += 1
                c = s[j]
        if s1 == s:
            return True

        return False
