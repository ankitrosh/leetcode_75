class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n = len(graph)
        m = len(graph[0])

        vis = [0]*n
        path_vis = [0]*n
        check = [0]*n
        
        res = []
        
        def dfs(graph, vis, path_vis, check,i):
            vis[i] = 1
            path_vis[i] = 1
            neighbours = graph[i]

            for j in neighbours:
                if vis[j] == 0:
                    if dfs(graph, vis, path_vis,check,j) == True:
                        check[j] = 0
                        return True
                elif path_vis[j] == 1:
                    check[j] = 0
                    return True
            
            path_vis[i] = 0
            check[i] = 1
            return False
        for i in range(n):
            if vis[i] == 0:
                dfs(graph,vis,path_vis,check,i)
        for i in range(n):
            
            if check[i] == 1:
                res.append(i)
        
        return res