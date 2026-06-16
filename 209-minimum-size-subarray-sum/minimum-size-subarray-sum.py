class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        curr_sum=0
        min_len=float('inf')#Infinity
        for r in range(len(nums)): #2 3 1 2 4 3
            curr_sum=curr_sum+nums[r]
            while curr_sum>=target:
                min_len=min(min_len,r-l+1)
                curr_sum-=nums[l]
                l+=1
        if min_len==float('inf'):
            return 0
        return min_len