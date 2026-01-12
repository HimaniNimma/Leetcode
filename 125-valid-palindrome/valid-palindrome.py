class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        temp=''
        for ch in s:
            if ch.isalnum():
                temp+=ch
        return temp[::-1]==temp