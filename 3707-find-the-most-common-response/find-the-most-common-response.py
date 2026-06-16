class Solution:
    def findCommonResponse(self, resp: List[List[str]]) -> str:
        d={}
        for s in resp:
            for key in set(s):
                if key in d:
                    d[key]+=1
                else:
                    d[key]=1
        freq=0
        res=-1
        for key,val in d.items():
            if freq<val:
                freq=val
                res=key
            elif freq==val and res>key:
                res=key
        return res