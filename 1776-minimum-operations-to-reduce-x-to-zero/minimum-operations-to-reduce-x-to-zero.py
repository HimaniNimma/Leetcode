class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target=sum(nums)-x
        if target==0:
            return len(nums)
        if target<0:
            return -1
        left=0
        longest=-1
        curr=0
        for r in range(len(nums)):
            curr+=nums[r]
            while curr >target:
                curr=curr-nums[left]
                left+=1
            if curr==target:
                longest=max(longest,(r-left+1))
        if longest==-1:
            return -1
        return len(nums)-longest