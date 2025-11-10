class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        distance = [[float('inf')]*n for _ in range(n)]

        for edge in edges:
            distance[edge[0]][edge[1]] = edge[2] 
            distance[edge[1]][edge[0]] = edge[2] 

        for i in range(n):
            distance[i][i] = 0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if distance[i][k] == float('inf') or distance[k][j] == float('inf'):
                        continue
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

        cityNum = -1
        countCity = n

        for city in range(n):
            cnt = 0
            for adjCity in range(n):
                if distance[city][adjCity] <= distanceThreshold:
                    cnt += 1
                
            if cnt <= countCity:
                countCity = cnt
                cityNum = city
        
        return cityNum




        