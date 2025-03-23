class Vertex:
    def __init__(self, key, x, y):
        self.key = key
        self.x = x
        self.y = y


class Graph:
    #? Khởi tạo bằng Hash Table
    def __init__(self):
        self.vertex_list = {}
        self.edges_list = {}
        
    """PHƯƠNG THỨC THÊM NÚT (VERTEX)
    """
    def add_vertex(self, item):
        
        vertex = Vertex(item['key'], item['X'], item['Y']) # add nút (vertex)  
        
        self.vertex_list[item['key']] = vertex
        
        if item['key'] not in self.edges_list:
            self.edges_list[item['key']] = set()
    
    """PHƯƠNG THỨC KIỂM TRA NÚT TỒN TẠI TRONG ĐỒ THỊ 
    """
    def validate_vertex(self, vertex):
        if vertex not in self.vertex_list:
            print("Vertex không tồn tại trong đồ thị!")
            return False

        return True
            
    """PHƯƠNG THỨC THÊM CẠNH (EDGE)
    
    #? vertex1: vị trí nút bắt đầu
    #? vertex2: vị trí nút kết thúc
    
    """
    def add_edge(self, vertex1, vertex2):
        if self.validate_vertex(vertex1["key"]) and self.validate_vertex(vertex2["key"]):
            # TH1: có hướng -> thêm vertex2 vào set của vertex 1
            self.edges_list[vertex1["key"]].add(vertex2["key"])
            
            # TH2: vô hướng -> thêm vertex1 vào set của vertex 2 (làm cả 2)
            self.edges_list[vertex2["key"]].add(vertex1["key"])
            
    def add_map_edge(self, vertex, neighbor_list):
        if self.validate_vertex(vertex):
            self.edges_list[vertex] = neighbor_list
    
    """PHƯƠNG THỨC TÌM NÚT KỀ VỚI NÚT ĐANG ĐỨNG (NEIGHBOR)
    
    #? vertex1: vị trí nút bắt đầu
    
    """
    def get_neighbor(self, vertex):
        if self.validate_vertex(vertex):
            return self.edges_list[vertex]
            
    
    """PHƯƠNG THỨC TÌM ĐƯỜNG ĐI (DEPTH FIRST SEARCH)"""
    def dfs(self, start, end, visited = None, path = None, result = None):
        # Khi mới bắt đầu duyệt -> tạo set visited rỗng, tạo path rỗng
        if visited is None:
            visited = set()

        if path is None:
            path = []
            
        if result is None:
            result = []

        visited.add(start)
        path.append(start)
        
        neighbors = self.get_neighbor(start)
        
        if start == end:
            for v in path:
                result.append(v)
            
        else: # Tìm neighbor của nút hiện tại
            for neighbor in neighbors:
                if neighbor not in visited:
                    self.dfs(neighbor, end, visited, path, result)
        
        path.pop()
        
        return result
        
    # def __str__(self):
    #     return str(self.edges_list)
    
graph = Graph()

#* BẢN ĐỒ
map = [
    {
        'key': 1,
        'X': 15,
        'Y': 15,
        'nei': [2, 6]
    },
    {
        'key': 2,
        'X': 130,
        'Y': 15,
        'nei': [1, 7]
    },
        {
        'key': 3,
        'X': 245,
        'Y': 15,
        'nei': [4, 8]
    },
        {
        'key': 4,
        'X': 360,
        'Y': 15,
        'nei': [3, 5]
    },
        {
        'key': 5,
        'X': 495,
        'Y': 15,
        'nei': [4]
    },

        {
        'key': 6,
        'X': 15,
        'Y': 130,
        'nei': [1, 11]
    },
        {
        'key': 7,
        'X': 130,
        'Y': 130,
        'nei': [2, 8]
    },
        {
        'key': 8,
        'X': 245,
        'Y': 130,
        'nei': [3, 7, 9]
    },
        {
        'key': 9,
        'X': 360,
        'Y': 130,
        'nei': [8, 10, 14]
    },
        {
        'key': 10,
        'X': 495,
        'Y': 130,
        'nei': [9, 15]
    },
        {
        'key': 11,
        'X': 15,
        'Y': 245,
        'nei': [6, 12, 16]
    },
    {
        'key': 12,
        'X': 130,
        'Y': 245,
        'nei': [11, 13]
    },
        {
        'key': 13,
        'X': 245,
        'Y': 245,
        'nei': [12, 18]
    },
        {
        'key': 14,
        'X': 360,
        'Y': 245,
        'nei': [9, 19]
    },
        {
        'key': 15,
        'X': 495,
        'Y': 245,
        'nei': [10]
    },
        {
        'key': 16,
        'X': 15,
        'Y': 360,
        'nei': [11, 17]
    },
        {
        'key': 17,
        'X': 130,
        'Y': 360,
        'nei': [16, 22]
    },
        {
        'key': 18,
        'X': 245,
        'Y': 360,
        'nei': [13, 23]
    },
        {
        'key': 19,
        'X': 360,
        'Y': 360,
        'nei': [14, 20]
    },
        {
        'key': 20,
        'X': 495,
        'Y': 360,
        'nei': [19, 25]
    },
        {
        'key': 21,
        'X': 15,
        'Y': 495,
        'nei': [22]
    },
        {
        'key': 22,
        'X': 130,
        'Y': 495,
        'nei': [17, 21]
    },
        {
        'key': 23,
        'X': 245,
        'Y': 495,
        'nei': [18]
    },
        {
        'key': 24,
        'X': 360,
        'Y': 495,
        'nei': [25]
    },
        {
        'key': 25,
        'X': 495,
        'Y': 495,
        'nei': [20, 24]
    }
]

for item in map:    
    graph.add_vertex(item)
    graph.add_map_edge(item['key'], item['nei']) # add cạnh (vertex)
    

print(graph.dfs(3, 23))
