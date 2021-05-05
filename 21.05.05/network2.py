#DFS
def solution(n, computers):
    answer = 0
    visited = []
    def DFS(temp):
        stack = [temp]
        while stack:
            s = stack.pop()
            if s not in visited:
                visited.append(s)
                for i in range(len(computers[temp])):
                    if computers[s][i] == 1 and i not in visited:
                        stack.append(i)
                        
    for i in range(len(computers)):
        if i not in visited:
            DFS(i)
            answer += 1
    return answer

#BFS
from collections import deque
def solution(n, computers):
    answer = 0
    visited = list()
    queue = deque()
    def BFS(temp):
        queue.append(temp)
        while queue:
            s = queue.popleft()
            if s not in visited:
                visited.append(s)
                for i in range(len(computers[temp])):
                    if computers[s][i] == 1 and i not in visited:
                        queue.append(i)
                        
    for i in range(len(computers)):
        if i not in visited:
            BFS(i)
            answer += 1
    return answer