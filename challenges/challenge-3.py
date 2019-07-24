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

    return data_struct
    # # Output code
    # print("# Vertices:", len(data_struct.vertices))
    #
    # all_edges = []
    # for vertex in data_struct.vertices: # O(n)
    #     for edges in vertex.edges: # O(m)
    #         all_edges.append((int(vertex.data), int(edges[0].data), edges[1]))
    #
    # print("# Edges:", len(all_edges))
    #
    # for edge in all_edges:
    #     print(edge)

if __name__ == '__main__':
    # read_text(file="/Users/timofeymakhlay/Documents/GitHub/cs-2.2/challenges/graph-data.txt")
    args = sys.argv[1:]
    graph = read_text(args[0])
    vert1 = args[1]
    vert2 = args[2]
    print(graph.getVertex("2").get_neighbors())
    print(vert1)
    print(vert2)

    path = graph.depth_first_search_path(vert1, vert2)

    print(path)
