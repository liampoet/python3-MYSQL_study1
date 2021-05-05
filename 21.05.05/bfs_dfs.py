'''
n개의 음이 아닌 정수가 있습니다. 
이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
'''
#bfs
from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    visited = list()
    while queue:
        t,n = queue.popleft()
        n += 1
        if n < len(numbers):
            queue.append([t + numbers[n],n])
            queue.append([t - numbers[n],n])
        else:
            if t == target:
                answer +=1
    return answer

#dfs
def solution(numbers, target):
    answer = 0
    stack = list()
    stack.append([numbers[0],0])
    stack.append([-1*numbers[0],0])
    visited = list()
    while stack:
        t,n = stack.pop()
        n += 1
        if n < len(numbers):
            stack.append([t + numbers[n],n])
            stack.append([t - numbers[n],n])
        else:
            if t == target:
                answer +=1
    return answer