class Solution:
    

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
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
        heapq.heappush(heap, PathObj(0,0,1))

        dx = [0, 1, 0, -1, 1, -1, 1, -1]
        dy = [1, 0, -1, 0, 1, -1, -1, 1]
        if grid[0][0] == 1:
            return -1
        while(len(heap) > 0):
            node = heapq.heappop(heap)

            for i in range(8):
                x =  node.x + dx[i]
                y = node.y + dy[i]

                if x >= 0 and x < n and y >= 0 and y < m:
                    if grid[x][y] == 0 and distance[x][y] > node.value +1:
                        heapq.heappush(heap, PathObj(x,y,node.value + 1))
                        if x == n-1 and y == m-1:
                            return node.value + 1
                     
                        distance[x][y] = node.value +1
        if n-1 == 0 and m-1 == 0:
            return 1
        return -1