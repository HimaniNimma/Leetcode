class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for ch in s:
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
        for key in d:
            if d[key]==1:
                return s.find(key)
        return -1