class Solution:
    def maxArea(self, height: List[int]) -> int:
        mA=0
        h,j=0,len(height) - 1
        while h<j:
            cA = min(height[h], height[j])*(j-h)
            mA=max(mA,cA)
            if height[h]< height[j]:
                h+=1
            else:
                j-=1
        return mA

            