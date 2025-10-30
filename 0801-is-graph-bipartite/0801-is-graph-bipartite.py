class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        n = len(graph)

        color = [-1]*n

        q = deque()

        
        for i in range(n):
            if color[i] == -1:
                q.append([graph[i], i])
                color[i] = 0
            while(len(q) > 0):
                [neighbors, node] = q.popleft()

                for i in neighbors:
                    if color[i] == -1:
                        color[i] = 1 - color[node]
                        q.append([graph[i], i])
                    elif color[i] == color[node]:
                        return False



        return True