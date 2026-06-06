class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        left=0
        longest=0
        max_count=0
        for r in range(len(s)):
            d[s[r]]=d.get(s[r],0)+1
            max_count=max(max_count,d[s[r]])
            while(r-left+1)-max_count>k:
                d[s[left]]-=1
                left+=1
            longest=max(longest,r-left+1)
        return longest