class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        
        visited = [0]*1001
        q = deque()

        q.append([start,0])

        while len(q) > 0:
            [x,steps] = q.popleft()

            if x == goal:
                return steps
            
            if 0 <= x <= 1000 and visited[x] == 1:
                continue
            
            if 0 <= x <= 1000:
                visited[x] = 1
            
            for num in nums:
                for new_x in (x+num, x-num,x^num):
                    if new_x == goal:
                        return steps + 1
                    if 0 <= new_x <= 1000 and visited[new_x] == 0:
                        q.append([new_x, steps+1])
                    
            
        return -1