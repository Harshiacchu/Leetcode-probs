# Leetcode: https://leetcode.com/problems/basic-calculator/description/
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def ev(i):
            r,d,n = 0,0,1
            while i < len(s):
                if s[i].isdigit():
                    d = d*10 + int(s[i])
                elif s[i] in ['+','-']:
                    r += d*n
                    d = 0
                    n = 1 if s[i] == '+' else -1
                elif s[i] == '(':
                    sr, i = ev(i+1)
                    r += n*sr
                elif s[i] == ')':
                    r += d*n
                    return r, i
                i+=1
            return r + d * n
        return ev(0)
