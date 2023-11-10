# Leetcode: https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits: List[str]) -> List[int]:
        n = ''
        for i in digits:
            n += str(i)
        
        n = int(n)+1
        return [int(i) for i in str(n)]
        
