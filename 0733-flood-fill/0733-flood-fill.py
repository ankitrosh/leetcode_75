class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        n = len(image)
        m = len(image[0])

        vis = []

        for i in range(n):
            lvl = [0]*m
            vis.append(lvl)
        old_color = image[sr][sc]
        def dfs(vis, i, j, n, m, image, color, old_color):
            vis[i][j] = 1
            image[i][j] = color
            if i + 1 < n and vis[i+1][j] == 0 and image[i+1][j] == old_color:
                dfs(vis, i+1,j,n,m,image,color,old_color)
            if i - 1 >= 0 and vis[i-1][j] == 0 and image[i-1][j] == old_color:
                dfs(vis, i-1,j,n,m,image,color,old_color)
            if j + 1 < m and vis[i][j+1] == 0 and image[i][j+1] == old_color:
                dfs(vis, i,j+1,n,m,image,color,old_color)
            if j -1 >= 0 and vis[i][j-1] == 0 and image[i][j-1] == old_color:
                dfs(vis, i,j-1,n,m,image,color,old_color)
        
        dfs(vis, sr,sc, n, m, image, color, old_color)

        return image



        