class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for i in range(n)]
        count = 1
        for row in range(n):
            #left to right
            for col in range(row,n-row):
                res[row][col] = count
                count += 1
            #top to bottom
            for col in range(row+1,n-row):
                res[col][n-row-1] = count
                count+=1
            #right to left
            for col in range(n-row-2,row-1,-1):
                res[n-row-1][col] = count
                count += 1
            #bottom to top
            for col in range(n-row-2,row,-1):
                res[col][row] = count
                count += 1
        return res

        
                


        