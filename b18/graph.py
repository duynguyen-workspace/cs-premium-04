import json

class Graph:
    #? Khởi tạo bằng Hash Table
    def __init__(self):
        self.adjacency_list = {}
        
    """PHƯƠNG THỨC THÊM NÚT (VERTEX)
    """
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = set()
    
    """PHƯƠNG THỨC KIỂM TRA NÚT TỒN TẠI TRONG ĐỒ THỊ 
    """
    def validate_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            print("Vertex không tồn tại trong đồ thị!")
            return False

        return True
            
    """PHƯƠNG THỨC THÊM CẠNH (EDGE)
    
    #? vertex1: vị trí nút bắt đầu
    #? vertex2: vị trí nút kết thúc
    
    """
    def add_edge(self, vertex1, vertex2):
        if self.validate_vertex(vertex1) and self.validate_vertex(vertex2):
            # TH1: có hướng -> thêm vertex2 vào set của vertex 1
            self.adjacency_list[vertex1].add(vertex2)
            
            # TH2: vô hướng -> thêm vertex1 vào set của vertex 2 (làm cả 2)
            self.adjacency_list[vertex2].add(vertex1)
            
    """PHƯƠNG THỨC XOÁ CẠNH (EDGE)
    
    #? vertex1: vị trí nút bắt đầu
    #? vertex2: vị trí nút kết thúc
    
    """
    def remove_edge(self, vertex1, vertex2):
        if self.validate_vertex(vertex1) and self.validate_vertex(vertex2):
            # TH1: có hướng -> thêm vertex2 vào set của vertex 1
            self.adjacency_list[vertex1].remove(vertex2)
            
            # TH2: vô hướng -> thêm vertex1 vào set của vertex 2 (làm cả 2)
            self.adjacency_list[vertex2].remove(vertex1)
    
    """PHƯƠNG THỨC TÌM NÚT KỀ VỚI NÚT ĐANG ĐỨNG (NEIGHBOR)
    
    #? vertex1: vị trí nút bắt đầu
    #? vertex2: vị trí nút kết thúc
    
    """
    def get_neighbor(self, vertex):
        if self.validate_vertex(vertex):
            return self.adjacency_list[vertex]
            
    
    """PHƯƠNG THỨC DUYỆT VERTEX THEO CHIỀU SÂU (DEPTH-FIRST TRAVERSAL)"""
    def dfs(self, vertex, visited = None):
        # Khi mới bắt đầu duyệt -> tạo set visited rỗng
        if visited is None:
            visited = set()

        visited.add(vertex)
        
        # In vertex ra
        # result += f"{vertex} -> "
        print(vertex, end=" -> ")
        
        neighbors = self.get_neighbor(vertex)
        
        # Tìm neighbor của nút hiện tại
        for neighbor in neighbors:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
    
    # def __str__(self):
    #     return str(self.adjacency_list)
    
graph = Graph()

# Add nút 1 -> 5
for v in range(1, 9):
    graph.add_vertex(v)
    
# Tạo cạnh
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(2, 6)
graph.add_edge(3, 7)
graph.add_edge(3, 8)
graph.add_edge(7, 5)
graph.add_edge(8, 5)
graph.add_edge(5, 6)
graph.add_edge(6, 4)

print(graph.adjacency_list)

# print(graph.get_neighbor(2))

graph.dfs(2)

