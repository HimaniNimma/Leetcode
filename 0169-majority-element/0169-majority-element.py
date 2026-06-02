class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for element in nums:
            if element not in d:
                d[element]=1
            else:
                d[element]+=1
        for key,value in d.items():
            if value>(len(nums)/2):
                return key