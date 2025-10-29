class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        res = 0
        vis = [0]*n
        def dfs(i, vis, isConnected, n):
            vis[i] = 1
            for j in range(n):
                if isConnected[i][j] == 1:
                    if vis[j] == 0:
                        dfs(j, vis, isConnected, n)

        for i in range(n):

            if vis[i] == 0:
                res += 1
                dfs(i, vis, isConnected, n)
            
        return res



        
        
        