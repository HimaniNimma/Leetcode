class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)%2==0:
            for i in range(0,len(nums)-2,3):
                print(nums[i],nums[i+1],nums[i+2])
                if nums[i]!=nums[i+1]==nums[i+2]:
                    return nums[i]
            return nums[-1]
        else:
            for i in range(0,len(nums)-3,3):
                print(nums[i],nums[i+1],nums[i+2])
                if nums[i]!=nums[i+1]==nums[i+2]:
                    return nums[i]
            return nums[-1]
        