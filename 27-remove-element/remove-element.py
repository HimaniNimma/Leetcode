class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        stack=[]
        for i in range(len(nums)):
            if nums[i]!=val:
                stack.append(nums[i])
        for i in range(len(stack)):
            nums[i]=stack[i]
        return len(stack)

