#Leetcode: https://leetcode.com/problems/reorganize-string/
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n, c = len(s), Counter(s)                             
        a = sorted([ch for ch in c], key = lambda x: -c[x]) 
        if c[a[0]] > (len(s)+1)//2: return ''              
        c1 = list(chain(*[[ch]*c[ch] for ch in a]))     
        return ''.join([c1[(n+i)//2] if i%2 else          
                        c1[i//2] for i in range(n)])
