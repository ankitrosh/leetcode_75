class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:

        n =  len(grid)
        m = len(grid[0])

        vis = []

        for i in range(n):
            lvl = [0]*m
            vis.append(lvl)

        def dfs(grid, vis, i, j, pi, pj, curr_val):
            print(i, j, pi, pj)
            vis[i][j] = 1
            n = len(grid)
            m = len(grid[0])

            # Down
            if i+1 < n and grid[i+1][j] == curr_val:
                if vis[i+1][j] == 0:
                    if dfs(grid, vis, i+1, j, i, j, curr_val):  # ✅ don't return immediately unless True
                        return True
                elif (i+1, j) != (pi, pj):
                    return True

            # Up
            if i-1 >= 0 and grid[i-1][j] == curr_val:
                if vis[i-1][j] == 0:
                    if dfs(grid, vis, i-1, j, i, j, curr_val):
                        return True
                elif (i-1, j) != (pi, pj):
                    return True

            # Right
            if j+1 < m and grid[i][j+1] == curr_val:
                if vis[i][j+1] == 0:
                    if dfs(grid, vis, i, j+1, i, j, curr_val):
                        return True
                elif (i, j+1) != (pi, pj):
                    return True

            # Left
            if j-1 >= 0 and grid[i][j-1] == curr_val:
                if vis[i][j-1] == 0:
                    if dfs(grid, vis, i, j-1, i, j, curr_val):
                        return True
                elif (i, j-1) != (pi, pj):
                    return True

            return False




        for i in range(n):
            for j in range(m):
               
                if vis[i][j] == 0:
                    print("================= ", i, j)
                    if dfs(grid, vis, i, j, -1, -1, grid[i][j]):
                        return True
        
        return False


