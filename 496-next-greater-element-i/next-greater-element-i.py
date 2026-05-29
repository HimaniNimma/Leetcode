class Solution:
    def nextGreaterElement(self, n1: List[int], n2: List[int]) -> List[int]:
        stack=[]
        for curr in n1:
            idx=n2.index(curr)
            greater=-1
            for j in range(idx+1,len(n2)):
                if n2[j]>curr:
                    greater=n2[j]
                    break
            stack.append(greater)
        return stack