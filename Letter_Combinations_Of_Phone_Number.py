# Leetcode: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {
            "" : "",
            1 : "",
            2 : "abc",
            3 : "def",
            4 : "ghi",
            5 : "jkl",
            6 : "mno",
            7 : "pqrs",
            8 : "tuv",
            9 : "wxyz"
        }
        if len(digits) == 1:
            return [i for i in d[int(digits)]]
        if len(digits) < 1:
            return []

        def map_char(char1,char2):
            l = []

            for i in char1:
                for j in char2:
                    l.append((i+j))
            return l
          
        def pass_char(digits):
            l = map_char(d[int(digits[0])],d[int(digits[1])])
            for i in range(2,len(digits)):
                l = map_char(l,d[int(digits[i])])
            return l
        return pass_char(digits)
