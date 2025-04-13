import heapq
import json

class Graph:
    def __init__(self):
        self.adjacency_list = {} # {"A": {"B": 2, "C": 3, ...}} -> khoảng cách những nút với nhau
        
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = {}
            
    def add_edge(self, from_vertex, to_vertex, distance):
        self.adjacency_list[from_vertex][to_vertex] = distance
        
        #! TH vô hướng
        self.adjacency_list[to_vertex][from_vertex] = distance
        
    def get_neighbors(self, vertex):        
        if vertex in self.adjacency_list:
            return self.adjacency_list[vertex] # Trả về dict là danh sách cạnh kề cùng trọng số
        
    def dijkstra(self, start, end):
        # 1. Dict khoảng cách từ nút start đến nút cần tới
        distance = {vertex: float('infinity') for vertex in self.adjacency_list}
        distance[start] = 0
        
        # 2. Dict chứa nút đứng trước để có được khoảng cách ngắn nhất
        previous = {vertex: None for vertex in self.adjacency_list}
        
        # 3. Hàng đợi ưu tiên
        priority_queue = [(0, start)]
        
        # 4. Danh sách vertex (nút) chưa duyệt
        unvisited_vertex = [vertex for vertex in self.adjacency_list]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            # Kiểm tra nếu đến được nút kết thúc
            if current_vertex == end:
                break
            
            # Kiểm tra nếu nút đã từng được duyệt chưa
            if current_vertex not in unvisited_vertex:
                continue
            
            neighbors = self.get_neighbors(current_vertex) # [{}, ]
            
            for key in neighbors:
                new_distance = current_distance + neighbors[key]
                
                if distance[key] == float('infinity') or new_distance < distance[key]:
                    # Cập nhật khoảng cách mới
                    distance[key] = new_distance
                    previous[key] = current_vertex
                    
                    heapq.heappush(priority_queue, (new_distance, key))
            
            # Duyệt hết nút kề -> xoá nút hiện tại khỏi mảng unvisited
            unvisited_vertex.remove(current_vertex)
    
        if previous[end] is None: 
            print("Không tìm thấy đường đi!")
            return None
    
        path = []
        vertex = end
        
        while vertex is not None:
            path.append(vertex)
            vertex = previous[vertex]
            
        path.reverse()
        return path
        
graph = Graph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")

    
# Tạo cạnh
graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 5)
graph.add_edge("B", "D", 9)
graph.add_edge("B", "E", 7)
graph.add_edge("B", "C", 11)
graph.add_edge("C", "E", 3)
graph.add_edge("D", "E", 13)
graph.add_edge("D", "F", 2)
graph.add_edge("E", "F", 6)

# print(graph.adjacency_list)

# {'A': {'B': 4, 'C': 5}, 'B': {'A': 4, 'D': 9, 'E': 7, 'C': 11}, 'C': {'A': 5, 'B': 11, 'E': 3}, 'D': {'B': 9, 'E': 13, 'F': 2}, 'E': {'B': 7, 'C': 3, 'D': 13, 'F': 6}, 'F': {'D': 2, 'E': 6}}

print(graph.dijkstra("F", "C"))