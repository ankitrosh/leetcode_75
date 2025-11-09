class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        adj = [[] for _ in range(n)]

        for road in roads:
            adj[road[0]].append([road[1], road[2]])
            adj[road[1]].append([road[0], road[2]])

        class PathObj:

            def __init__(self, node, time):
                self.node = node
                self.time =time
            
            def __lt__(self, other):

                if self.time == other.time:
                    return self.node < other.node
                
                return self.time < other.time
        
        heap = []
        distance  = [float('inf')]*n
        ways = [0]*n
        distance[0] = 0
        ways[0] = 1
        heapq.heappush(heap, PathObj(0,0))

        while len(heap) > 0:
            pathNode = heapq.heappop(heap)
            node = pathNode.node
            time = pathNode.time
            for neighbour in adj[node]:
                nextNode, pathWeight = neighbour
                if distance[nextNode] > time + pathWeight:
                    ways[nextNode] = ways[node]
                    distance[nextNode] = time + pathWeight
                    heapq.heappush(heap, PathObj(nextNode, time+pathWeight))

                elif distance[nextNode] == time + pathWeight:
                        ways[nextNode] = int((ways[nextNode] + ways[node])%(1e9 + 7))
                    
        
        return ways[n-1]

        
