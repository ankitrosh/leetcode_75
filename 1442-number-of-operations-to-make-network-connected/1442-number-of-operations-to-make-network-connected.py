class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        adj = [[] for _ in range(n)]
        vis = [0]*n
        num_edges = 0
        for c in connections:
            adj[c[0]].append(c[1])
            adj[c[1]].append(c[0])
            num_edges += 1

        def dfs(adj, i, vis):
            vis[i]  = 1
            for neighbour in adj[i]:
                if vis[neighbour] == 0:
                    dfs(adj, neighbour, vis)
        res = 0
        for i in range(n):
            if vis[i] == 0:
                print(i)
                res += 1
                dfs(adj, i, vis)
        print(res, num_edges)
        if n - 1 <= num_edges:
            return res -1 
        
        return -1