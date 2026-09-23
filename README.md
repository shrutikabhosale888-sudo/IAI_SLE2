# SLE-2: BFS vs DFS Campus Navigation Profiling

**Name:** Shrutika Bhosale  
**PRN:** 25UAM073  
**Course:** 02AML204 – Introduction to Artificial Intelligence

## Overview

This project compares Breadth-First Search (BFS) and Depth-First Search (DFS) using a small college campus navigation graph.

Each campus building is represented as a node and each path is represented as an edge.

Both algorithms are tested on the same graph to make the comparison fair.
## Objective

The objectives are:

1. Implement BFS and DFS.
2. Test both algorithms on the same graph.
3. Measure execution time.
4. Count nodes expanded.
5. Compare Best, Average and Worst cases.
6. Use py-spy for additional profiling.

## Problem Statement

A student starts from the college Main Gate and needs to find different buildings on campus.

The campus is represented using a graph.

The search algorithms are used to find the destination building.

## Graph


                         Gate
                       /      \
                  Admin       Library
                  /   \       /     \
                Lab Canteen Auditorium Garden
               / \    / \       |       |
       Classroom1 Classroom2 Hostel1 Hostel2 Sports Parking

Start Node: Gate

Best Case: Admin

Average Case: Hostel1

Worst Case: Parking

Algorithms
BFS

BFS explores nodes level by level.

It uses a Queue.

DFS

DFS explores one branch deeply before backtracking.

It uses a Stack.

Tools Used
Python
timeit
Manual node counter
py-spy
Experimental Results

Run benchmark_cases.py and record the actual values.

Case	Goal	BFS Time (ms)	BFS Nodes	DFS Time (ms)	DFS Nodes
Best Case	Admin	Actual	Actual	Actual	Actual
Average Case	Hostel1	Actual	Actual	Actual	Actual
Worst Case	Parking	Actual	Actual	Actual	Actual
Project Files
File	Description
campus_search.py	Campus graph, BFS and DFS implementation
benchmark.py	Execution-time comparison
benchmark_cases.py	Best, Average and Worst Case analysis
profile_search.py	Program used for py-spy profiling
campus_profile.svg	py-spy flame graph
README.md	Project documentation
AI_CONTRIBUTION_LOG.md	AI usage record
.gitignore	Prevents unwanted files from being uploaded
How to Run
Run the search
python campus_search.py
Run benchmark
python benchmark.py
Run case analysis
python benchmark_cases.py
Generate py-spy profile
py-spy record --output campus_profile.svg -- python profile_search.py
Conclusion

This experiment demonstrates the practical comparison of BFS and DFS using execution time and nodes expanded.

The experiment also shows how different goal positions can affect the behavior of search algorithms.
