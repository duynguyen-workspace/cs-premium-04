import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}
        
        # self.adjacency_list = {} # {"A": {"B": 2, "C": 3, ...}}
        
        
    def add_node(self, value):
        self.nodes.add(value)
        
    def add_edge(self, from_node, to_node, distance):
        self.edges.setdefault(from_node, []).append(to_node)
        self.distances[(from_node, to_node)] = distance
        
    def dijkstra(self, start):
        paths = {}
        visited = {start: 0}
        distance = 0
        
        heap = [(0, start)]
        nodes = set(self.nodes)
        
        while nodes and heap:
            current_weight, min_node = heapq.heappop(heap)
            try:
                nodes.remove(min_node)
            except KeyError:
                pass
        
            for edge in self.edges.get(min_node, []):
                weight = current_weight + self.distances[(min_node, edge)]
                
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight 
                    paths[edge] = min_node
                    heapq.heappush(heap, (weight, edge))
        
        return paths, visited
    
    def get_path(self, start, end):
        paths, distance = self.dijkstra(start) # A
        
        route = [end] # F
        
        while end != start:
            if end in paths:
                end = paths[end]
                route.append(end)
            else:
                print("Cannot found exited path")
                return None
            
        route.reverse()
        return route, distance[route[-1]]
        
graph = Graph()

graph.add_node("S")
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_node("F")

graph.add_edge("A", "B", 2)
graph.add_edge("A", "C", 4)
graph.add_edge("B", "C", 1)
graph.add_edge("B", "D", 3)
graph.add_edge("C", "E", 3)
graph.add_edge("D", "F", 1)
graph.add_edge("E", "D", 2)
graph.add_edge("E", "F", 5)

# graph.add_edge("S", "A", 3)
# graph.add_edge("S", "C", 2)
# graph.add_edge("S", "F", 6)
# graph.add_edge("A", "B", 6)
# graph.add_edge("A", "D", 1)
# graph.add_edge("B", "E", 1)
# graph.add_edge("C", "A", 2)
# graph.add_edge("C", "D", 3)
# graph.add_edge("D", "E", 4)
# graph.add_edge("F", "E", 2)


# print(str(graph.distances))

start, end = "A", "F"

route, total_time = graph.get_path(start, end)
print(f"Path from {start} to {end}: {route} - time: {total_time}")



