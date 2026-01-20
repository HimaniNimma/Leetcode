class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for ele in nums:
            if ele not in d:
                d[ele]=1
            else:
                d[ele]+=1
        for key,value in d.items():
            if value>(len(nums)/2):
                return key