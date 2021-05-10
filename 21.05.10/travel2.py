def dfs(graph, N, path, here):
    path.append(here)
    
    if len(path) == N + 1:
        return True
    
    if here not in graph:
        path.pop()
        return False
    
    for i in range(len(graph[here])):
        there = graph[here][-1]
        graph[here].pop()
        
        if dfs(graph, N, path, there):
            return True
        
        graph[here].insert(0, there)
        
    path.pop()
    return False

def solution(tickets):
    routes = dict()

    for (start, end) in tickets:
        routes[start] = routes.get(start, []) + [end]  
    
    for r in routes.keys():
        routes[r].sort(reverse=True)
    
    N = len(tickets)
    path = []
    
    if dfs(routes, N, path, "ICN"):
        answer = path            
        
    return answer

if __name__ == '__main__':
    tickets = [
        ["ICN", "JFK"], 
        ["HND", "IAD"], 
        ["JFK", "HND"]
    ]
    result = solution(tickets)
    print(result)