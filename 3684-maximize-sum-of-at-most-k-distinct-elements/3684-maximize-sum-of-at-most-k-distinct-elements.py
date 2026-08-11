class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        l= sorted(set(nums), reverse=True)
        
        return l[:k]