# Graph Propertied

* Problems are often represented through existence, instance, enumeration, or optimization of a property.
  * `Existence`: Does the graph have this property?
    * **EX:** Is there a path in graph G? (Yes, by definition every graph has at least one path)
    * **EX:** Is there a path of length 5 in G?
  * `Instance`: Find an example of the property in the graph.
    * **EX:** Find a path from vertex u to vertex v in G. List the vertices in the path.
  * `Enumeration`: How many instances of the property exist in the graph?
    * **EX:** How many paths of length 5 exist in G?
  * `Optimization`: Find a minimum or maximum instance of the property
    * **EX:** What is the longest path in G?
* Graph algorithms are used to find the existence, instance, enumeration or optimization of graph properties.

A **characteristic** of a graph can be defined in terms of its vertices, edges or both.
Path - Cannot repeat the same edges or vertices.
Order - The order of a graph is its number of vertices.
Size -  The size of a graph is its number of edges.
Cycle - path that ends with start vertex.
Diameter - the greatest distance between any pair of vertices.
Vertex Cut - Removing a vertex from the graph rendering it disconnected (Vertexes without edges).
Vertex Connectivity - is the size of a minimal vertex cut. (Number of Vertex cuts until it becomes disconnected).
Edge Connectivity - Number of edges that can be removed until it becomes edge-disconnected.
Vertex Coloring - Color coding vertices so no two same color vertices share the same edge. (Loop-less graphs only).
Chromatic Number - The smallest number of colors needed to color a graph.
Clique -  is a subset of vertices of an undirected graph such that every two distinct vertices in the clique are adjacent; that is, its induced subgraph is complete.
Clique Number - The number of vertices in a clique.
Acyclic - Contains no cycle.
