from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        queue = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        minutes = 0
        while queue and fresh > 0:
            minutes += 1
            for i in range(len(queue)):
                p,q = queue.popleft()


                for x,y in directions :
                    nx,ny = p+x,q+y
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx,ny))
                        fresh -= 1
        if fresh == 0:
            return minutes
        else:
            return -1

        