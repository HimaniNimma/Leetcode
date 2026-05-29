class Solution:
    def nextGreaterElement(self, n1: List[int], n2: List[int]) -> List[int]:
        stack=[]
        for num in n1:
            idx=n2.index(num)
            nxt=-1
            for j in range(idx+1,len(n2)):
                if n2[j]>num:
                    nxt=n2[j]
                    break
            stack.append(nxt)
        return stack