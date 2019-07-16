# coding: utf-8
#!python
# graph.py
# By Timofey Makhlay (github.com/timomak/cs-2.2)

class ArrayVertex(object):
    def __init__(self, data):
        """
        Initialize the Vertex with the given data.
        Running: O(1)
        """
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
        Runtime: O(n)
        """
        if self.getVertex(vertKey=vert) != None:
            raise ValueError("Vertex with this key already exists.")

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
        return None

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
        Running: O(n) because of getVertex()
        """
        current_vert = self.getVertex(x)

        return current_vert.edges

    def find_path(self, start_vertex, end_vertex, path=None):
        """
        Setup for the function to work properly.
        Running: O(n^3)
        """
        if path == None:
            path = []
        start_vertex = self.getVertex(start_vertex)
        end_vertex = self.getVertex(end_vertex)
        return self._find_path_recursive(start_vertex, end_vertex, path)

    # Got this idea from: https://www.python-course.eu/graphs_python.php
    def _find_path_recursive(self, start_vertex, end_vertex, path=None):
        """
        Find a path from start_vertex to end_vertex in graph.
        Recursive loop.
        Runtime: O(n^3)
        """
        path = path + [start_vertex]

        if start_vertex.data == end_vertex.data:
            return path


        for (vertex, weight) in start_vertex.edges: # O(n)
            if vertex not in path: # O(n)
                extended_path = self._find_path_recursive(vertex, end_vertex, path) # O(n)
                if extended_path:
                    return extended_path
        return None

    def breadth_first_search(self, vertex, n = 0):
        """
        Find all neightboring nodes n edges away from the provided vertex.
        Running: O(n^2)
        """
        explored = [] # All the neighbors

        start = self.getVertex(vertex) # Checking if the start Vertex is in the graph. O(n)

        queue = [] # Queue to track the current Vertex we're exploring.

        queue.append(start) # O(1)

        counter = 0 # To stop at the right depth.

        while queue: # While not Empty. O(m)
            vert = queue.pop(0) # Dequeue the first in queue.O(m)

            if vert not in explored: # If it wasn't already explored. O(x)
                explored.append(vert) # Add it to explored. O(1)
                edges = vert.edges # Add it's neighbors to the queue. O(1)

                for edge in edges:
                    queue.append(edge[0]) # Because we have tuples (Vertex('1'), weight).
            counter += 1
            if counter == n and n > 0:
                return explored
        return explored


graph = ArrayGraph()

graph.addVertex("1")
graph.addVertex("2")
graph.addVertex("3")
print("Graph:", graph.vertices)
print("Adding Edget from 1 to 2")
graph.addEdge("1", "2",0)

print("Adding Edget from 2 to 3")
graph.addEdge("2", "3",0)

print(graph.breadth_first_search("1", 3))
