class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        D1={}
        D2={}
        for ch in s:
            if ch in D1 :
                D1[ch]+=1
            else:
                D1[ch]=1
        for ch in t:
            if ch in D2:
                D2[ch]+=1
            else:
                D2[ch]=1
        if len(D1)!=len(D2):
            return False
        for ch in D1:
            if ch not in D2 or D1[ch]!=D2[ch]:
                return False
        return True
