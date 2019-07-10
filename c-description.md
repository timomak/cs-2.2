# Challenges

1. [General Instructions](#general-instructions)
1. [Challenge 1](#challenge-1)
1. [Challenge 2](#challenge-2)
1. [Challenge 3](#challenge-3)
1. [Challenge 4](#challenge-4)
1. [Challenge 5](#challenge-5)


## General instructions
- Your code should go in the Challenge Folder of your personal repo that you created for this class.
- Your code should meet the following minimum requirements
    - meets PEP8 style guidelines
    - is well tested
    - is well documented
    - cites any sources used for inspiration  and clearly indicates what code is used / modified from these sources

- Unless otherwise stated, use simple concrete data types in your implementations (lists, dictionaries). Stretch challenges will give you an opportunity to refactor with collections and more complex data types.

- Each challenge will read in a graphs from a text file with
    - the first line being a G or D (for graph or digraph)
    - the second line being a list of vertices,
    - remaining lines are one vertex pair per line representing the edges `(x,y)` or a triplet if there are weights ``(x, y, w)``

```
G
1,2,3,4
(1,2)
(1,4)
(2,3)
(2,4)
```

- Each challenge should be run from the command line and provide output in the format requested.

- Your code should be in at least two files.  File 1 must be named challege-X.py where X is the challenge number.  This file will be run from the command line with arguments of the graph text file and (possibly) additional arguments needed for the challenge.  `python3 challenge-1.py graph-data.txt`

- Other files should follow best practices for code architecture (classes in a file with the class name, etc) but the structure is up to you.

- You will be graded on if your code works (produces the correct output), and code quality based on the [Challenge Rubric]()

## Challenge 1
- Implement the Graph ADT with an adjacency list
- Implement code to read in a graph from a text file to create an instance of the Graph ADT and use it's methods.

**Input:** A graph file (can contain a directed or undirected graph with or without  weights)

**Output:**
* The # vertices in the graph.
* The # edges in the graph.
* A list of the edges with their weights (if weighted)


### Stretch Challenges 1
- Re-implement the Graph ADT using one of the [python collections](https://docs.python.org/3.6/library/collections.html#module-collections)

## Challenge 2
- Add properties to your Graph ADT


## Challenge 3
- DFS and BFS

### Stretch Challenges 3

## Challenge 4
- Dijkstra's Algorithm

### Stretch Challenges 4 : Implement Priority Queue
- (From CS 2.1).  Implement BinaryMinHeap using a dynamic array and then implement Priory Queue using BinaryMinHeap.  See [binary heap starter code](https://github.com/Make-School-Courses/CS-2.1-Advanced-Trees-and-Sorting-Algorithms/blob/master/Code/binaryheap.py) and [priority queue starter code](https://github.com/Make-School-Courses/CS-2.1-Advanced-Trees-and-Sorting-Algorithms/blob/master/Code/priorityqueue.py) for outline.
- Dynamic Programming


## Challenge 5
- Coloring, Scheduling

### Stretch Challenges 5
- Dynamic Programming

## Challenge 6
- Dynamic Programming


### Stretch Challenges 6
- - NP Reduction
