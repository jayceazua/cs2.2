## Challenge 2

**Create a Challenge_2 folder in your challenge repository.  Copy any code you want to re-use from Challenge 1 to that folder before modifying**

Update your Graph ADT code to use Breadth-first search to compute the shortest path between two provided vertices in your graph.  

**Input:** A graph file (containing an undirected, unweighted graph), a from_vertex and a to_vertex.

`python3 challenge_2.py graph_data.txt 1 5`

```
G
1,2,3,4,5
(1,2)
(1,4)
(2,3)
(2,4)
(2,5)
(3,5)
```

**Output:**
The vertices in a shortest path from `from_vertex` to `to_vertex` and the number of edges in that path.
```
Vertices in shortest path: 1,2,5
Number of edges in shortest path: 2

```
### [Challenge 2 Rubric](https://www.makeschool.com/rubrics/UnVicmljLTk=)