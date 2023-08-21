# Leetcode: https://leetcode.com/problems/rearrange-words-in-a-sentence/

class Solution(object):
    def arrangeWords(self, s):
        """
        :type text: str
        :rtype: str
        """
        
        # a = []
        # for i in s.split(" "):
        #     a.append(i.lower())
        return " ".join(sorted(s.split(" "),key=len)).capitalize()
            
        
