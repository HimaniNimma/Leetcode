class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels='AEIOUaeiou'
        i=0
        j=len(s)-1
        l=list(s)
        while(i<j):
            if s[i] in vowels and s[j] in vowels:
                temp=l[i]
                l[i]=l[j]
                l[j]=temp
                i+=1
                j-=1
            if s[i] not in vowels:
                i+=1
            if s[j] not in vowels:
                j-=1
        return ''.join(l)
            
