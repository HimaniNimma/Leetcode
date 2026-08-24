class Solution:
    def maxFreqSum(self, s: str) -> int:
        vow={}
        cons={}
        vowels={'a','e','i','o','u'}
        a=0
        b=0
        for i in s:
            if i in vowels:
                if i in vow:
                    vow[i]+=1
                else:
                    vow[i]=1
                a=max(a,vow[i])
            else:
                if i in cons:
                    cons[i]+=1
                else:
                    cons[i]=1
                b=max(b,cons[i])
        return a+b

