from typing import List
class Solution:
    def sortColors(self, n: List[int]) -> None:
        start=0
        mid=0
        end=len(n)-1
        while mid<=end:
            if n[mid]==0:
                n[start],n[mid]=n[mid],n[start]
                start+=1
                mid+=1
            elif n[mid]==1:
                mid+=1
            else:
                n[mid],n[end]=n[end],n[mid]
                end-=1