# Counting Cycles in a Graph Using an Adjacency Matrix

This is a Python program which takes an adjacency matrix as input and uses it to count the number of cycles in the graph.
It also outputs the length of the longest cycle, the longest cycle itself, and the number of layers in the graph.

```
e.g

0 1 0 0 0 0 0 0 0 0 0 0 0
1 0 1 0 0 0 0 0 0 0 0 0 0
0 1 0 1 1 0 0 0 0 0 0 0 0
0 0 1 0 0 1 1 0 0 0 0 0 0
0 0 1 0 0 1 0 0 1 0 0 0 0
0 0 0 1 1 0 0 0 0 1 0 0 0
0 0 0 1 0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 1 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0 1 0 1 1
0 0 0 0 0 0 0 0 0 0 1 0 1
0 0 0 0 0 0 0 0 0 0 1 1 0

Number of cycles: 2
Longest Cycle: 4 nodes | ['3', '4', '6', '5']
Number of layers in the graph: 7
```