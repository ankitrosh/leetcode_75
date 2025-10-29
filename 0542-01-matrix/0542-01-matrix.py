class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        n = len(mat)
        m = len(mat[0])

        vis = [[0]*m for _ in range(n)]

        res = [[0]*m for _ in range(n)]

        q = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    vis[i][j] = 1
                    q.append([i, j, 0])
        
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        while len(q) > 0:
            [i,j, steps] = q.popleft()
            res[i][j] = steps
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                
                if x < n and x >= 0 and y < m and y >= 0:
                    if vis[x][y] == 0:
                        vis[x][y] = 1
                        q.append([x,y,steps+1])
            
        return res 