from collections import deque

# Campus graph
graph = {
    "Gate": ["Admin", "Library"],
    "Admin": ["Lab", "Canteen"],
    "Library": ["Auditorium", "Garden"],

    "Lab": ["Classroom1", "Classroom2"],
    "Canteen": ["Hostel1", "Hostel2"],

    "Auditorium": ["Sports"],
    "Garden": ["Parking"],

    "Classroom1": [],
    "Classroom2": [],
    "Hostel1": [],
    "Hostel2": [],
    "Sports": [],
    "Parking": []
}


# BFS
def bfs(graph, start, goal):
    queue = deque([start])
    visited = set()
    nodes_expanded = 0

    while queue:
        current = queue.popleft()

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            return True, nodes_expanded

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)

    return False, nodes_expanded


# DFS
def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    nodes_expanded = 0

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            return True, nodes_expanded

        for neighbor in reversed(graph[current]):
            if neighbor not in visited:
                stack.append(neighbor)

    return False, nodes_expanded


# Test
start = "Gate"
goal = "Parking"

bfs_found, bfs_nodes = bfs(graph, start, goal)
dfs_found, dfs_nodes = dfs(graph, start, goal)

print("======== BFS RESULTS ========")
print("Goal found:", bfs_found)
print("Nodes expanded:", bfs_nodes)

print("\n======== DFS RESULTS ========")
print("Goal found:", dfs_found)
print("Nodes expanded:", dfs_nodes)