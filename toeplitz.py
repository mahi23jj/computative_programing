class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        x=True
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
              if matrix[i-1][j-1]!=matrix[i][j]:
                x=False
                break
        return x  
