## Challenge 3

Update your Graph ADT code to do the following
1. Implement Recursive Depth-first search to determine if there is a path between two vertices in a **directed** graph.  

**Input:** A file containing a directed graph, a from_vertex and a to_vertex.

`python3 challenge_3.py graph_data.txt 1 5`

```
D
1,2,3,4,5
(1,2)
(1,4)
(2,3)
(2,4)
(3,5)
(5,2)
```

**Output:**
If there is a path between the vertices (T/F) and the vertices in that path.
```
There exists a path between vertex 1 and 5: TRUE
Vertices in the path: 1,2,3,5


```

### Stretch Challenges 3 : Dijkstra's and Priority Queue
**Stretch Challenge 3.1** Implement Dijkstra's Algorithm to find the minimum weight path between two vertices in a weighted undirected graph.

**Input:** A file containing a weighted undirected graph, a from_vertex and a to_vertex.

`python3 challenge_3.py graph_data.txt 1 5`

```
G
1,2,3,4,5
(1,2,4)
(1,4,5)
(2,3,6)
(2,4,9)
(2,5,6)
(3,5,10)
```

**Output:**
The vertices in a minimum weight path between the vertices and the weight of that path.
```

The weight of the minimum weight path between vertex 1 and 5 is: 10
Vertices in the path: 1,2,5
```

**Stretch Challenge 3.2** (From CS 2.1).  Implement BinaryMinHeap using a dynamic array and then implement Priory Queue using BinaryMinHeap.  See [binary heap starter code](https://github.com/Make-School-Courses/CS-2.1-Advanced-Trees-and-Sorting-Algorithms/blob/master/Code/binaryheap.py) and [priority queue starter code](https://github.com/Make-School-Courses/CS-2.1-Advanced-Trees-and-Sorting-Algorithms/blob/master/Code/priorityqueue.py) for outline.


### [Challenge 3 Rubric](https://docs.google.com/document/d/1VHCcs3rFtrIaJRT5GWL3P-m3oagptYXuA2T9O67eJQU/preview)
