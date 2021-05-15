from collections import deque
class Solution:
    def orange(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        q = deque([])
        visited = set()
        graph = [[-1 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([[i, j], 0])
                    graph[i][j] = 0
                    visited.add((i, j))
        
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        
        while q:
            curr, value = q.popleft()
            x, y = curr
            for i, j in zip(dx, dy):
                nx, ny = x + i, y + j
                if 0 <= nx < m and 0 <= ny < n:
                    if (nx, ny) not in visited and grid[nx][ny] == 1:
                        visited.add((nx, ny))
                        q.append([[nx, ny], value+1])
                        graph[nx][ny] = value + 1
        
        answer = 0
        for i in range(m):
            for j in range(n):
                answer = max(answer, graph[i][j])
                if grid[i][j] == 1 and graph[i][j] == -1:
                    return -1
        return answer
