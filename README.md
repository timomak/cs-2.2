# CS 2.2 Graphs
> Introduction to Graph Theory

# [Slides](https://docs.google.com/presentation/d/1eOGVRA2ziw9swgB1t0VXn2_gnIWl1sd-H5xglgSa3-E/edit?usp=sharing)


##  Why you should know this...
Graph theory is a powerful tool for developing algorithmic thinking and modeling real world problems. Today we will get a glimpse of how we can use this tool by exploring both algorithms and modeling and then merging these together.   


## Learning Objectives (5 min)

1. Practice modeling real world problems with graph theory.
1. Implement algorithms from graph theory with diagrams and pseudocode.
1. Define the Graph ADT and implement in code.

## Activity 1: Model & Implement [40 min]
- With your pair, choose a Model or Implement scenario from the list.  
- [15 min] Using pseudocode, diagrams, whiteboards, etc. complete your scenario.
- [5 min] Find another pair whose scenario maps to yours.   
- [15 min] Swap scenarios with the other pair
- [5 min] Discuss the solutions

## Course Overview [20 min]
- Go over syllabus, learning outcomes, course policies, key deliverables.
- Our course learning approach: Model, Implement Solution, Synthesize & Algorithmic Thinking

## BREAK [10 min]

## Overview 2: Graphs & Digraphs [10 min]
- A **graph** is a collection of **vertices** (also called nodes) and a collection of **edges** which connect one vertex to another.  An edge from vertex *u* to vertex *v* is represented by the unordered pair *(u,v)* and is the same as an edge from *v* to *u*.   
    - Unless otherwise noted, the term **graph** will represent a **undirected simple graph** which has at most one edge between two vertices, and no **loops** or edges from a vertex to itself.

- A **digraph** (directed graph) is a collection of **vertices** and a collection of **arcs** (also called directed edges) which connect one vertex to another with an ordering.  An arc from vertex *u* to *v* can be represented by the ordered pair *(u,v)* and this is different than an arc from vertex *v* to *u* represented as *(v,u)* .

- A **weighted graph (or digraph)** is a graph (digraph) with weights assigned to its edges (arcs).  The weight of an edge is denoted *w(u,v)* and can represent a variety of properties like distance, time, or cost.  


## Activity 2: Graph Implementation [10 min]
In pairs, write pseudocode to store and process a graph.
- What data structure(s) should you use?
- Does your structure allow weights? Edge direction?
- What things might you want to compute on a graph and how does this affect your data structure?
- How well does your structure support finding a path from vertex *u* to vertex *v*?

## Overview 3: Graph Representation
There are many ways to represent a graph, the decision of which method to use is based on what you want to do with the graph.  Most programming languages (including python) don't have a **graph** data structure.  So we'll use the **Graph Abstract Data Type (ADT)** as a basis to define our own.

The Graph ADT is defined as follows:
```python

Graph() #creates a new, empty graph.
addVertex(vert) #adds an instance of Vertex to the graph.
addEdge(fromVert, toVert) #Adds a new, directed edge to the graph that connects two vertices.
addEdge(fromVert, toVert, weight) #Adds a new, weighted, directed edge to the graph that connects two vertices.
getVertex(vertKey) #finds the vertex in the graph named vertKey.
getVertices() #returns the list of all vertices in the graph.
getNeighbors(x) # lists all vertices y such that there is an edge from the vertex x to the vertex y;

```


The implementation of the Graph ADT includes making choices about how to store the vertices and edges.  We'll explore three methods:


- **Edge List:** A graph is defined by its vertices and edges, so the simplest way to represent it is a list of vertices and a list of edges.  
    - Positive: Easy to build.
    - Negative: Time to look up (`O(E)`).

- **Adjacency Matrix:** A graph is defined by a matrix with rows and columns representing vertices and entries of 1 if an edge exist and 0 if not.
    - Positive: Easy to find, add, delete vertices or edges (`O(1)`)
    - Negative: Space use is more than necessary (`O(V^2)`) especially as most graphs are sparse.

- **Adjacency List:** A graph is defined by an array of linked lists indicating which vertices are adjacent to each other. Each vertex is an index with its adjacent vertices stored in a linked list.
    - Positives: Easy to solve graph traversal problems
    - Negatives: Time to find edges is slightly more than in adjacency matrix.



## Activity 3: Implement the Graph ADT [40 min]
 - Start on Challenge 1 with your pair.



## Wrap Up (5 min)

- Review Learning Outcomes
- Overview of homework and topics for next class

## Challenges
- [Challenge 1](../Challenges/Challenges.md#challenge-1)) : Implement the Graph ADT

## Interview Questions
- Given this graph, how would you represent it in code?
- [Clone a graph](https://leetcode.com/problems/clone-graph/)

## Resources:
- [A Gentle Introduction To Graph Theory](https://medium.com/basecs/a-gentle-introduction-to-graph-theory-77969829ead8)
- [Graph Theory](https://en.wikipedia.org/wiki/Graph_theory#Route_problems)
- [From Theory To Practice: Representing Graphs](https://medium.com/basecs/from-theory-to-practice-representing-graphs-cfd782c5be38)
- [How to think in graphs](https://medium.com/free-code-camp/i-dont-understand-graph-theory-1c96572a1401)
- [Visualgo Graphs](https://visualgo.net/en/graphds)
