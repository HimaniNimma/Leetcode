class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        total=0
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for key,val in dic.items():
            if val==1:
                total+=key
        return total