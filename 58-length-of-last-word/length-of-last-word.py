class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list=s.split()
        return len(list[-1])