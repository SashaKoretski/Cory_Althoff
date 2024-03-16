import heapq


class Vertex:
    def __init__(self, key):
        self.key = key
        self.connections = {}

    def add_adj(self, vertex, weight=0):
        self.connections[vertex] = weight

    def get_connections(self):
        return self.connections.keys()

    def get_weight(self, vertex):
        return self.connections[vertex]


class Graph:
    def __init__(self):
        self.vertex_dict = {}

    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vertex_dict[key] = new_vertex

    def get_vertex(self, key):
        if key in self.vertex_dict:
            return self.vertex_dict[key]
        return None

    def add_edge(self, f, t, weight=0):
        if f not in self.vertex_dict:
            self.add_vertex(f)
        if t not in self.vertex_dict:
            self.add_vertex(t)
        self.vertex_dict[f].add_adj(self.vertex_dict[t], weight)


def dijkstra(graph_1, vertex_1, vertex_2):
    distance = {vertex: float('infinity') for vertex in graph_1}
    distance[vertex_1] = 0
    pq = [(0, vertex_1)]

    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distance[current_vertex]:
            continue

        for neighbor, weight in graph_1[current_vertex].items():
            distance = current_distance + weight
            if distance < distance[neighbor]:
                distance[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distance[vertex_2]


graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_edge("A", "B", 1)
graph.add_edge("B", "C", 10)
# graph = {
#     "A": {"B": 2, "C": 6},
#     "B": {"D": 5},
#     "C": {"D": 8},
#     "D": {}
# }
print(dijkstra(graph, graph.get_vertex("A"), graph.get_vertex("B")))
# for vertex in graph:
#     print(vertex)
