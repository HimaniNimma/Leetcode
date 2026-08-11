class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        d1 = {}
        for i in ransomNote:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for j in magazine:
            if j in d1:
                d1[j] += 1
            else:
                d1[j] = 1
        for i in d:
            if d[i] > d1.get(i, 0):
                return False
        return True