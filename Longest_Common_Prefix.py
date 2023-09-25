# Leetcode: https://leetcode.com/problems/longest-common-prefix/description/
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        

        if len(strs) == 0:
            return ""
        
        if len(strs)  == 1:
            return strs[0]

        result = strs[0]
        length = len(result)
    
        for i in range(1, len(strs)):
            while strs[i].find(result) != 0:
                result = result[:length - 1]
                length -= 1
    
                if not result:
                    return ""
    
        return result
