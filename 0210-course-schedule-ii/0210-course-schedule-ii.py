class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]

        for u,v in prerequisites:
            adj[u].append(v)

        
        inDegrees = [0]*numCourses

        for i in range(numCourses):
            for e in adj[i]:
                inDegrees[e] += 1
        

        q = deque()

        for i in range(numCourses):
            if inDegrees[i] == 0:
                q.append(i)
        
        topo = []
        while (len(q) > 0):
            node = q.popleft()
            topo.append(node)
            neigbours = adj[node]

            for e in neigbours:
                inDegrees[e] -= 1
                if(inDegrees[e] == 0):
                    q.append(e)

        if len(topo) != numCourses:
            return []
        
        topo.reverse()
        return topo