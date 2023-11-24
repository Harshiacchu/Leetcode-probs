# Leetcode: https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        #sort is done to the get the max no of coins while iterating
        piles.sort()

        res = 0
        
        for i in range(len(piles)//3, len(piles),2):
            res += piles[i]
        return res

      
