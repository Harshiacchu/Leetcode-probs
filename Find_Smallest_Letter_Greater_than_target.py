class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = letters
        t = target
        j = ""
        for i in l:
            if i>t:
                j = i
                break
        
        return j if j!="" else l[0]
