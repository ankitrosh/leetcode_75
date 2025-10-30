class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        n = len(board)
        m = len(board[0])

        vis = [[0]*m for _ in range(n)]

        def dfs(board, vis, i, j):
            print(i, j, board[i][j])
            vis[i][j] = 1

            xd = [1, 0, -1, 0]
            yd = [0, 1, 0, -1]

            for k in range(4):
                x = i + xd[k]
                y = j + yd[k]
                if x < n and x >= 0 and y < m and y >= 0:
                    if vis[x][y] == 0 and board[x][y] == "O":
                        dfs(board, vis, x, y)

        for j in range(m):
            if vis[0][j] == 0 and board[0][j] == "O":
                dfs(board, vis, 0, j)

        for j in range(m):
            if vis[n-1][j] == 0 and board[n-1][j] == "O":
                dfs(board, vis, n-1, j)

        for i in range(n):
            if vis[i][0] == 0 and board[i][0] == "O":
                dfs(board, vis, i, 0)

        for i in range(n):
            if vis[i][m-1] == 0 and board[i][m-1] == "O":
                dfs(board, vis, i, m-1)

        
        for i in range(n):
            for j in range(m):
                print(i, j, vis[i][j], board[i][j])
                if board[i][j] == "O" and vis[i][j] == 0:
                    board[i][j] = "X"
                
        
