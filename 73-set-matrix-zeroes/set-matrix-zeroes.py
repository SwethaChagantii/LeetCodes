class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # 0,0   0,1   0,2
        # 1,0   1,1   1,2
        # 2,0   2,1   2,2
        rows = len(matrix)
        col = len(matrix[0])
        row_zero = set()
        col_zero = set()
        for i in range(rows):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_zero.add(i)
                    col_zero.add(j)
        for i in range(rows):
            for j in range(col):
                if i in row_zero or j in col_zero:
                    matrix[i][j] = 0

            
        return matrix
        
        