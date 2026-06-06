class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left=0
        zero=0
        res=0
        for r in range(len(nums)):
            if nums[r]==0:
                zero+=1
            while zero>1:
                if nums[left]==0:
                    zero-=1
                left+=1
            res=max(res,r-left)
        return res