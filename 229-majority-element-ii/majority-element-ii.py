class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l=[]
        d={}
        for ele in nums:
            if ele not in d:
                d[ele]=1
            else:
                d[ele]+=1
        for key in d:
            if d[key]>(len(nums)//3):
                l.append(key)
        return l