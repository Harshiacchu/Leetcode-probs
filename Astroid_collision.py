class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
       
        p = []
        m = []
        for a in asteroids:
            if a > 0:
                p.append(a)
            else:
                while p and p[-1] < abs(a):
                    p.pop()
                if not p:
                    m.append(a)
                elif p[-1] == abs(a):
                    p.pop()
                
        return m + p
