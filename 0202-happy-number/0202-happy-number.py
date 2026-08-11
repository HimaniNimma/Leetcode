class Solution:
    
    def isHappy(self, n: int) -> bool:
        l=[]
        while n>0:
            t=0
            while n>0:
                d=n%10
                t+=d**2
                n//=10
            if(t==1):
                return True
            else:
                if t in l:
                    return False
                l.append(t)
                n=t
