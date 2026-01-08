class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count=0
        if(a<b):
            v=a
        else:
            v=b
        for i in range(1,v+1):
            if (a%i ==0 and b%i==0):
                count+=1
        return count