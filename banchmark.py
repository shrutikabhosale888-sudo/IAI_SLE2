import timeit
from bfs_dfs import graph, bfs, dfs


def measure(algorithm, start, goal, repetitions=1000):

    def run():
        algorithm(graph, start, goal)

    total = timeit.timeit(run, number=repetitions)
    average = (total / repetitions) * 1000

    found, nodes = algorithm(graph, start, goal)

    return average, nodes, found


cases = {
    "Best Case": "Admin",
    "Average Case": "Hostel1",
    "Worst Case": "Parking"
}


print("==============================================")
print(" BFS vs DFS CASE ANALYSIS")
print("==============================================")

for case, goal in cases.items():

    print("\n----------------------------------------------")
    print(case)
    print("Goal Node:", goal)
    print("----------------------------------------------")

    bfs_time, bfs_nodes, bfs_found = measure(
        bfs, "Gate", goal
    )

    dfs_time, dfs_nodes, dfs_found = measure(
        dfs, "Gate", goal
    )

    print("\nBFS:")
    print("Average Time:", round(bfs_time, 6), "ms")
    print("Nodes Expanded:", bfs_nodes)
    print("Goal Found:", bfs_found)

    print("\nDFS:")
    print("Average Time:", round(dfs_time, 6), "ms")
    print("Nodes Expanded:", dfs_nodes)
    print("Goal Found:", dfs_found)