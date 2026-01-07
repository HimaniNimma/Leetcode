class Solution:
    def addDigits(self, n: int) -> int:
        s=0
        tot=0
        if n<=0:
            return n
        while n>0:
            tot=0
            while n>0:
                s=n%10
                tot+=s
                n//=10
            if tot<10:
                return tot
            else:
                n=tot
                