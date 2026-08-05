class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for optr in operations:
            if "++X" == optr or "X++"== optr:
                x+=1
            else:
                x-=1
        return x