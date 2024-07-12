graph = {
    'A': ['B', 'C'], 
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'], 
    'D': ['B'], 
    'E': ['B', 'F'], 
    'F': ['C', 'E']
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            neighbours = graph[node]
            for neighbour in neighbours:
                if neighbour not in visited:
                    stack.append(neighbour)

# Test
dfs(graph, 'A')
