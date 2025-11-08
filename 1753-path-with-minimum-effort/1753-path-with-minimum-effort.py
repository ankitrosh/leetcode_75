class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        class PathObj:
            def __init__(self, x, y, value):
                self.value = value
                self.x = x
                self.y = y

            def __lt__(self, other):
                return self.value < other.value

            def __repr__(self):
                return f"PathObj({self.value})"
        distance = [[float('inf')]*m for _ in range(n)]
        distance[0][0] = 0
        heap = []
        heapq.heappush(heap, PathObj(0,0,0))

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        while(len(heap) > 0):
            node = heapq.heappop(heap)

            for i in range(4):
                x =  node.x + dx[i]
                y = node.y + dy[i]
                if x >= 0 and x < n and y >= 0 and y < m:
                    effort = max (abs(heights[node.x][node.y] - heights[x][y]), node.value )
                    if distance[x][y] > effort:
                        heapq.heappush(heap, PathObj(x,y,effort))
                     
                        distance[x][y] = effort

        return distance[n-1][m-1]