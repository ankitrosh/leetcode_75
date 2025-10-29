class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = []

        for i in range(n):
            lvl = [0]*m
            vis.append(lvl)
        q = deque()
        
        def mark_adj(grid, vis, i, j,q):
            vis[i][j] = 1
            
            if i + 1 < n and vis[i+1][j] == 0 and grid[i+1][j] == 1:
                grid[i+1][j] = 2
                vis[i+1][j] =1
                q.append([i+1,j])
            if i - 1 >= 0 and vis[i-1][j] == 0 and grid[i-1][j] == 1:
                grid[i-1][j] = 2
                vis[i-1][j] = 1
                q.append([i-1,j])
            if j + 1 < m and vis[i][j+1] == 0 and grid[i][j+1] == 1:
                grid[i][j+1] = 2
                vis[i][j+1] = 1
                q.append([i,j+1])
            if j - 1 >= 0 and vis[i][j-1] == 0 and grid[i][j-1] == 1:
                grid[i][j-1] = 2
                vis[i][j-1] = 1
                q.append([i,j-1])

        res = 0
        oranges_there = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2 and vis[i][j] == 0:
                    vis[i][j] = 1
                    q.append([i,j])
                if grid[i][j] != 0:
                    oranges_there += 1
                    
        if oranges_there == 0:
            return 0
        while len(q) > 0:
            res += 1
            size = len(q)
            for i in range(size):
                [i, j] = q.popleft()
                
                mark_adj(grid, vis, i, j, q)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        
        return res-1
                    
