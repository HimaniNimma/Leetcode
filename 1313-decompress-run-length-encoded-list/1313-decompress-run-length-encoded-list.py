class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result=[]
        n=len(nums)
        for i in range(0,n,2):
            freq=nums[i]
            val=nums[i+1]
            result=result+[val]*freq
            #res.extend([val]*freq)
        return result