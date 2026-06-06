class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites=0
        for right in range(k):
            if blocks[right]=="W":
                whites+=1
        res=whites
        left=0
        for right in range(k,len(blocks)):
            if blocks[right]=="W":
                whites+=1
            if blocks[left]=="W":
                whites-=1
            left+=1
            res=min(res,whites)
        return res