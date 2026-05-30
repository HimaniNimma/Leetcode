class Solution:
    def trap(self, h: List[int]) -> int:
        n=len(h)
        l=[0]*n
        r=[0]*n
        l[0]=h[0]
        for i in range(1,n):
            l[i]=max(l[i-1],h[i])
        r[n-1]=h[n-1]
        for i in range(n-2,-1,-1):
            r[i]=max(r[i+1],h[i])
        w=0
        for i in range(n):
            w+=min(l[i],r[i])-h[i]
        return w