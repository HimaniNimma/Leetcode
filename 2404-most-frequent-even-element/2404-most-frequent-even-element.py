class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d={}
        for n in nums:
            if n%2 == 0:
                if n in d:
                    d[n]+=1
                else:
                    d[n]=1
        print(d)
        freq=0
        res=-1
        for k,v in d.items():
            if freq<v:
                freq=v
                res=k
            elif freq==v and res>k:
                res=k
        return res