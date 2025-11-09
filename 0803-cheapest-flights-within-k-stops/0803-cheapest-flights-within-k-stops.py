class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        class PathObj:
            def __init__(self, stops, node, value):
                self.value = value
                self.stops = stops
                self.node = node

            def __lt__(self, other):
                if self.stops == other.stops:
                    if self.node == other.node:
                        return self.value < other.value
                    else:
                        return self.node < other.node
                return self.stops < other.stops
        adj = [[] for _ in range(n)]

        for item in flights:
            adj[item[0]].append([item[1], item[2]])
        heap = []
        distance  = [float('inf')]*n
        heapq.heappush(heap, PathObj(0, src, 0))
        distance[src] = 0

        while (len(heap) > 0):
            station = heapq.heappop(heap)
            stops = station.stops
            node = station.node
            val = station.value

            if stops > k:
                continue
            
            for neighbours in adj[node]:
                nextStop = neighbours[0]
                cost = neighbours[1]

                if cost + val < distance[nextStop] and stops <= k:
                    distance[nextStop] = cost + val
                    heapq.heappush(heap, PathObj(stops+1,nextStop, cost+val))
                

        if distance[dst] == float('inf'):
            return -1
        
        return distance[dst]
