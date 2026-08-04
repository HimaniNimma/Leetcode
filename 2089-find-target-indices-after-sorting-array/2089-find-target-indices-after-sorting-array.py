class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        s = sorted(nums)
        arr=[]
        for i in range(len(s)):
            if s[i]==target:
                arr.append(i)
        return arr