class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        s = [True]*n 
        s[0] = s[1] = False
        p = 2
        while p * p < n:
            if s[p]:
                for i in range(p * p, n, p):
                    s[i] = False
            p += 1
        return sum(s)  

