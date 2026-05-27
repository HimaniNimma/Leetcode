class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        d=0
        for ch in s:
            if ch=="(":
                if d>0:
                    stack.append(ch)
                d+=1
            else:
                d-=1
                if d>0:
                    stack.append(ch)
        return ''.join(stack)
