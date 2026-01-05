class Solution:
    def isValid(self, s: str) -> bool:
        l = list(s)
        stack  = []
        for ch in l:
            if ch in "({[":
                stack.append(ch)
            elif ch in ")}]":
                if not stack:
                    return False
                if (ch == ')' and stack[-1] != '(') or \
                   (ch == '}' and stack[-1] != '{') or \
                   (ch == ']' and stack[-1] != '['):
                    return False
                stack.pop()
        return len(stack) == 0
