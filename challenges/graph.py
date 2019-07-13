# coding: utf-8
#!python
# graph.py
# By Timofey Makhlay (github.com/timomak/cs-2.2)

class ArrayVertex(object):
    def __init__(self, data):
        """Initialize the Vertex with the given data."""
        self.data = data
        self.edges = []

    def __repr__(self):
        """Return a string represenation of this Vertex"""
        return 'Vertex({!r})'.format(self.data)

class ArrayGraph(object):
    def __init__(self, iterable=None):
        """
        Initialize this Array Graph and append the given items, if any.
        Runtime: O(1) if no items. O(items) with items.
        """
        self.vertices = []
        self.size = 0

        # Add vertices if provided.
        if iterable is not None:
            for item in iterable:
                self.addVertex(item)

    def __repr__(self):
        """Return a string representation of this graph."""
        return 'Graph({!r})'.format(self.getVertices())

    def addVertex(self, vert):
        """
        Adds an instance of Vertex to the graph.
        Runtime: O(1)
        """
        new_vert = ArrayVertex(vert)
        self.vertices.append(new_vert)
        self.size += 1

    def addEdge(self, fromVert, toVert, weight=0):
        """
        Adds a new, weighted, directed edge to the graph that connects two vertices.
        Runtime: O(number of vertices) + O(number of edges in fromVert)
        """
        if fromVert == toVert:
            raise ValueError("Can't create an edge with the same Vertex.")

        start = None
        end = None

        counter = 0

        for vert in self.vertices: # O(n)
            if vert.data == fromVert:
                start = counter
            elif vert.data == toVert:
                end = counter
            counter += 1

        if start == None:
            raise ValueError(fromVert, " is not a Vertex.")
        if end == None:
            raise ValueError(toVert, " is not a Vertex.")

        try:
            weight = int(weight)
        except ValueError:
            raise ValueError("The weight has to be an integer.")


        for edge in self.vertices[start].edges: # O(n)
            if edge == (self.vertices[end], weight):
                raise ValueError("The Edge already exists")

        self.vertices[start].edges.append((self.vertices[end], weight))


    def getVertex(self, vertKey):
        """
        Finds the vertex in the graph named vertKey.
        Runtime: O(n) for vertices.
        """
        for vert in self.vertices: # O(n)
            if vert.data == vertKey:
                return vert

        raise ValueError("The vertex doesn't exist.")

    def getVertices(self):
        """
        Returns the list of all vertices in the graph.
        Runtime: O(1)
        """
        return self.vertices


    def getNeighbors(self, x):
        """
        Lists all vertices y such that there is an edge from the vertex x to the vertex y.

        """
        pass

    def find_path(self, start_vertex, end_vertex, path=None):
        """Setup for the function to work properly"""
        if path == None:
            path = []
        start_vertex = self.getVertex(start_vertex)
        end_vertex = self.getVertex(end_vertex)
        return self.find_path_recursive(start_vertex, end_vertex, path)

    # Got this idea from: https://www.python-course.eu/graphs_python.php
    def find_path_recursive(self, start_vertex, end_vertex, path=None):
        """
        Find a path from start_vertex to end_vertex in graph.
        Recursive loop.
        Runtime: O(n^2)
        """
        path = path + [start_vertex]

        if start_vertex.data == end_vertex.data:
            return path


        for (vertex, weight) in start_vertex.edges: # O(n)
            if vertex not in path: # O(n)
                extended_path = self.find_path_recursive(vertex, end_vertex, path)
                if extended_path:
                    return extended_path
        return None


# graph = ArrayGraph()
# print("Empty Graph:", graph.vertices)
# print("Adding Vertex 1-3")
# graph.addVertex("1")
# graph.addVertex("2")
# graph.addVertex("3")
# print("Graph:", graph.vertices)
# print("Adding Edget from 1 to 2")
# graph.addEdge("1", "2",0)
# print("All the neighbors of Vertex 1:",graph.vertices[0].edges)
# print("Find path between 1 and 2")
# print(graph.find_path(start_vertex="1", end_vertex="2"))
#
#
# print("Adding Edget from 2 to 3")
# graph.addEdge("2", "3",0)
# print("All the neighbors of Vertex 2:",graph.vertices[1].edges)
# print("Find path between 1 and 3")
# print(graph.find_path(start_vertex="1", end_vertex="3"))
