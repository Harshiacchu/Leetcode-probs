class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        a = {}
        if len(pattern)!= len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in a and s[i] not in a.values():
                a[pattern[i]] = s[i]
        
        for i in range(len(pattern)):
            if pattern[i] in a.keys():
                if a[pattern[i]] != s[i]:
                    return False
            else:
                return False
    
        return True


