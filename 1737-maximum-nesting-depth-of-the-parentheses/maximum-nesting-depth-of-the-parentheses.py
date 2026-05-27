class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        max_d=0
        for i in s:
            if i=="(":
                stack.append(i)
                max_d=max(max_d,len(stack))
            elif i==")" and stack:
                stack.pop(
                    
                )
        return max_d
            