class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])

        vis = [[0]*m for _ in range(n)]

        q = deque()

        for i in range(n):
            
            if grid[i][0] == 1:
                q.append([i,0])
                vis[i][0] = 1
        
            if grid[i][m-1] == 1:
                q.append([i,m-1])
                vis[i][m-1] = 1
        
        for j in range(m):
            
            if grid[0][j] == 1:
                q.append([0,j])
                vis[0][j] = 1
        
            if grid[n-1][j] == 1:
                q.append([n-1,j])
                vis[n-1][j] = 1
        
        while(len(q) > 0):
            [i, j] = q.pop()

            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]

            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]

                if(x < n and x >= 0 and y < m and y >= 0):
                    if grid[x][y] == 1 and vis[x][y] == 0:
                        q.append([x,y])
                        vis[x][y] = 1
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and vis[i][j] == 0:
                    res+=1
        
        return res
