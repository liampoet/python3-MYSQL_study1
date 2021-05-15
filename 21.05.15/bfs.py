class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        
        answer = [[0 for _ in range(n)] for _ in range(m)]
        q = collections.deque([])
        
        visited = set()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    q.append([[i, j], 0])
                    visited.add((i, j))
        
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        
        while q:
            curr, value = q.popleft()
            x, y = curr
            for i, j in zip(dx, dy):
                nx = x + i
                ny = y + j
                if 0 <= nx < m and 0 <= ny < n:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append([[nx, ny], value+1])
                        answer[nx][ny] = value + 1
        
        return answer