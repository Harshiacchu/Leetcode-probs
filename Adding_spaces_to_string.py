# Leetcode: https://leetcode.com/problems/adding-spaces-to-a-string/
class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """

        # TLE issue
        # i = 0
        # c = 0
        # while(i<len(spaces)):

        #     s = s[:spaces[i]] + " " + s[spaces[i]:]
        #     c += 1
        #     if i+1 < len(spaces):
        #         spaces[i+1] = spaces[i+1]+c
        #     # print(spaces)
        #     i += 1
        # return s

      #TLE issue
        # res = s[:spaces[0]] + " "
        # print(res)
        # for i in range(1,len(spaces)):
        #     res += s[spaces[i-1]:spaces[i]] + " "
            
        # res += s[spaces[-1]:]
        # return res
        
        res = []
        l = 0
        for i in spaces:
            res.append(s[l:i] )
            l = i
        res.append(s[l:])
        return " ".join(res)
