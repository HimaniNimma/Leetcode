class Solution:
    def calculate(self, s: str) -> int:
        n,sign,stack =0,1,[]
        res=0
        for i in s:
            if i.isdigit():
                n=n*10+int(i)
            elif i==' ':
                continue
            elif i == "+":
                res=res+sign*n
                sign=1
                n=0
            elif i == "-":
                res=res+sign*n
                sign=-1
                n=0               
            elif i == "(":
                stack.append(res)
                stack.append(sign)
                res=0
                sign=1
            elif i==")":
                res+=sign*n
                n=0
                res=res*stack.pop()
                res=res+stack.pop()
        return res+sign*n