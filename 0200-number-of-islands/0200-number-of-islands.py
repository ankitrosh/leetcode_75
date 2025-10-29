class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
       

        def dfs(vis, m, n, grid, i, j):
            vis[i][j] = 1
            if i+1 < m:
                if vis[i+1][j] == 0 and grid[i+1][j] == "1":
                    dfs(vis, m, n, grid, i+1, j)
            if i-1 >= 0:
                if vis[i-1][j] == 0 and grid[i-1][j] == "1":
                    dfs(vis, m, n, grid, i-1, j)
            if j+1 < n :
                if vis[i][j+1] == 0 and grid[i][j+1] == "1":
                    dfs(vis, m, n, grid, i, j+1)
            if j -1 >= 0:
                if vis[i][j-1] == 0 and grid[i][j-1] == "1":
                    dfs(vis, m, n, grid, i, j-1)
            
        m = len(grid)
        n = len(grid[0])
        vis = []
        for i in range(m):
            level = [0]*n
            for j in range(n):
                level[j] = 0
            vis.append(level)
        
        res = 0
        for i in range(m):
            for j in range(n):
                # print(grid[i][j], vis[i][j])
                
                if grid[i][j] == "1" and vis[i][j] == 0:
                    print("in")
                    res+=1
                    dfs(vis, m,n, grid, i, j)
        
        return res