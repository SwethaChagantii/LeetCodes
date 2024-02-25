class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    print(matrix[i][j],target)
                    count = 1
                    break
        if count == 1:
            return True
        else:
            return False
        