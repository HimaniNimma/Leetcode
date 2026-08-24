class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg=sum(nums)/len(nums)
        h=max(1,int(avg)+1)
        while h in nums:
            h+=1
        return h        
        