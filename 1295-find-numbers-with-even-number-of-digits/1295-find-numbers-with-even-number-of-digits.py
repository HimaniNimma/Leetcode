class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        digit_count=0
        for i in range(len(nums)):
            even_count=0
            n=nums[i]
            while n>0:
                r=n%10
                even_count+=1
                n=n//10
            if even_count%2==0:
                digit_count+=1
        return digit_count
                