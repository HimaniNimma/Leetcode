class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rl=len(matrix)
        cl=len(matrix[0])
        for row in range(rl):
            for col in range(cl):
                if matrix[row][col]==0:
                    for i in range(cl):
                        if matrix[row][i]!=0:
                            matrix[row][i]='x'
                    for i in range(rl):
                        if matrix[i][col]!=0:
                            matrix[i][col]='x'
        for row in range(rl):
            for col in range(cl):
                if matrix[row][col]=='x':
                    matrix[row][col]=0  
        for k in matrix:
            print(*k)            
