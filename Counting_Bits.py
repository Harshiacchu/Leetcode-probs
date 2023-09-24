# Leetcode: https://leetcode.com/problems/counting-bits/
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l = []
        for i in range(0,n+1):
            l.append((bin(i)).count('1'))
        return l
