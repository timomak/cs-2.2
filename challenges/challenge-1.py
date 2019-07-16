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

from graph import ArrayGraph
import sys

def read_text(file):
    file = open(file, "r")

    counter = 0
    data_struct = None
    temp_verices = []
    temp_edges = []

    for line in file:
        if counter is 0: # First line
            if line.strip().upper() == "G":
                data_struct = ArrayGraph()
            elif line.upper() == "D":
                pass
        elif counter is 1: # Second line
            temp_verices = line.strip().split(',')
            for vert in temp_verices:
                data_struct.addVertex(vert)
        else: # All the edges
            tuple = eval(line.strip())

            temp_edges.append(tuple)

            if len(tuple) == 3: # If it has weight
                data_struct.addEdge(str(tuple[0]), str(tuple[1]), tuple[2])
            else:
                data_struct.addEdge(str(tuple[0]), str(tuple[1]))


        counter += 1

    # Output code
    print("# Vertices:", len(data_struct.vertices))

    all_edges = []
    for vertex in data_struct.vertices: # O(n)
        for edges in vertex.edges: # O(m)
            all_edges.append((int(vertex.data), int(edges[0].data), edges[1]))

    print("# Edges:", len(all_edges))

    for edge in all_edges:
        print(edge)


if __name__ == '__main__':
    # read_text(file="/Users/timofeymakhlay/Documents/GitHub/cs-2.2/challenges/graph-data.txt")
    args = sys.argv[1:]
    read_text(args[0])
