class Solution:
    def numSpecial(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        li1 = [0]*m
        li2 = [0]*n
        count = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    li1[i] += 1 # li1 0=1  1=1 2=1
                    li2[j] += 1 # li2 0=2  2=1

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1 and li1[i] == 1 and li2[j] == 1:
                    count += 1
                        
        return count
        
        