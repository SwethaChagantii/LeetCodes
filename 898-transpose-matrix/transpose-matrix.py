class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        arr = [[0 for i in range(n)] for j in range(m)] 
        for i in range(m):
            for j in range(n):
                arr[i][j] = matrix[j][i]
        return arr
        