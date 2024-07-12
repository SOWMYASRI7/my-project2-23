from collections import deque

graph = {
    'A': ['B', 'C'], 
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'], 
    'D': ['B'], 
    'E': ['B', 'F'], 
    'F': ['C', 'E']
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        neighbours = graph[node]
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)

# Test
bfs(graph, 'A')
