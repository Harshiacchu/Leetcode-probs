# Leetcode: https://leetcode.com/problems/count-primes/description/
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        ip = [True]*n
        ip[0] = ip[1] = False
        for i in range(2,int(n**0.5)+1):
            if ip[i]:
                for j in range(i*i,n,i):
                    ip[j] = False
                    # print(j)
        return sum(ip)        
