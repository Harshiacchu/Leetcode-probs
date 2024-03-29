# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/description/
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref) == 1:
            return pref
        
        return [pref[0]] + [pref[i] ^ pref[i-1] for i in range(1,len(pref))]
        
