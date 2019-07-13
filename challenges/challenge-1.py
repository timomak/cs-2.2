# Graph() #creates a new, empty graph.
# addVertex(vert) #adds an instance of Vertex to the graph.
# addEdge(fromVert, toVert) #Adds a new, directed edge to the graph that connects two vertices.
# addEdge(fromVert, toVert, weight) #Adds a new, weighted, directed edge to the graph that connects two vertices.
# getVertex(vertKey) #finds the vertex in the graph named vertKey.
# getVertices() #returns the list of all vertices in the graph.
# getNeighbors(x) # lists all vertices y such that there is an edge from the vertex x to the vertex y;

# Challenge 1: Make a graph out of a text file.

## 1st line: Is it a graph or diagram ("G" or " D")
## 2nd line: List of all the Vertices (nodes "1,2,4,5")
## 3rd line: tuples of the edges (the lines connecting the Vertices [nodes]). "(1,2) or (1,4,5) [the third is the weight]"

"""
Pseudocode for make_graph_from(textfile):
1. Open the file and read each line.
    * Use the first line to run Graph. (Graph())
    * Use the second line to add Vertex. (addVertex())
    * Use the rest to create Edges. (addEdge())
"""

"""
Resources:
1. Github Class repo: https://github.com/Make-School-Courses/CS-2.2-Advanced-Recursion-and-Graphs/blob/master/Challenges/Challenges.md
2. Graphs in Python Explanation: https://www.python-course.eu/graphs_python.php
3. StackOverflow Graphs: https://stackoverflow.com/questions/19472530/representing-graphs-data-structure-in-python
"""
