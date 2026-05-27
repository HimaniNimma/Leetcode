class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def check(p):
            stack=[]
            for i in p:
                if i!="#":
                    stack.append(i)
                elif stack and i=="#":
                    stack.pop()
            return ''.join(stack)
        return check(s)==check(t)