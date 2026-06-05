class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        res=[0]*n
        if k==0:
            return [0]*n
        start,end=(1,k) if k>0 else (n+k,n-1)
        window_sum=sum(code[start:end+1])
        for i in range(n):
            res[i]=window_sum
            window_sum-=code[start%n]
            start+=1
            end+=1
            window_sum+=code[end%n]
        return res