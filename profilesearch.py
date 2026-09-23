from bfs_dfs import graph, bfs, dfs

print("Starting BFS profiling...")

for _ in range(1000):
    bfs(graph, "Gate", "Parking")

print("BFS profiling completed.")

print("Starting DFS profiling...")

for _ in range(1000):
    dfs(graph, "Gate", "Parking")

print("DFS profiling completed.")

print("Profiling program finished.")