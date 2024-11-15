class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n=len(matrix)
        m=len(matrix[0])
        res=[[0]*n for _ in range(m)]
        for j in range(m):
            for i in range(n):
                res[j][i]=matrix[i][j]
        return res 
