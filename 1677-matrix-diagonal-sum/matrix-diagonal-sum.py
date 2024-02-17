class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        res = 0
        size = len(mat)
        for i in range(size):
            sum = sum + mat[i][i] 
        for i in range(size):
            if i != size-i-1:
                res = res + mat[i][size-i-1]
        return sum + res 
        