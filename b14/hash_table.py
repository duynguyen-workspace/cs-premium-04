import json

class Product:
    def __init__(self, name, price, image, category):
        self.name = name
        self.price = price
        self.image = image
        self.category = category

class AVLNode:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None
        self.height = 1
        
class AVLTree:
    def __init__(self):
        self.root = None
        
    """
    PHƯƠNG THỨC: LẤY CHIỀU CAO CỦA 1 NÚT 
    """    
    def get_height(self, node):
        if not node:
            return 0
        
        return node.height
    
    """
    PHƯƠNG THỨC: TÍNH (CẬP NHẬT) CHIỀU CAO LỚN NHẤT CỦA 1 NÚT 
    """    
    def update_height(self, node):
        if not node:
            return 0
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        
    """
    PHƯƠNG THỨC: TÍNH ĐỘ CÂN BẰNG CỦA 1 NÚT
    """
    def get_balance(self, node):
        if not node:
            return 0
        
        return self.get_height(node.left) - self.get_height(node.right)
    
    """
    PHƯƠNG THỨC: XOAY PHẢI VÀ XOAY TRÁI NÚT
    """
    def right_rotate(self, tree_not_balance):
        # Tách cây
        left_child = tree_not_balance.left
        sub_tree = left_child.right
        
        # Thế chỗ phù hợp cho nút lệch và nút gần kề
        left_child.right = tree_not_balance
        tree_not_balance.left = sub_tree
        
        # Cập nhật chiều cao cho cây vừa cân bằng
        self.update_height(tree_not_balance)
        self.update_height(left_child)
        
        # Trả về giá trị cây vừa cân bằng
        return left_child
    
    def left_rotate(self, tree_not_balance):
        # Tách cây
        right_child = tree_not_balance.right
        sub_tree = right_child.left
        
        # Thế chỗ phù hợp cho nút lệch và nút gần kề
        right_child.left = tree_not_balance
        tree_not_balance.right = sub_tree
        
        # Cập nhật chiều cao cho cây vừa cân bằng
        self.update_height(tree_not_balance)
        self.update_height(right_child)
        
        # Trả về giá trị cây vừa cân bằng
        return right_child
    
    def insert(self, value):
        # Khi chưa có nút rễ -> mình sẽ gán giá trị của nút rễ là 1 node mới
        if self.root == None:
            self.root = AVLNode(value)
        else:
            self.root = self._insert_recursive(self.root, value)
            
        # print(f"Thêm thành công {value}")
        
    def _insert_recursive(self, node, value):
        #! Khi chưa có con
        if not node:
            return AVLNode(value)

        #* Khi phát hiện có nút đang tồn tại
        if value < node.key:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.key:
            node.right = self._insert_recursive(node.right, value)
        else:
            return node
        
        # Cập nhật chiều cao tại vị trí nút được thêm vào
        self.update_height(node)
        
        # Tính độ cân bằng
        balance = self.get_balance(node)
        
        #? TH1: lệch trái - trái
        if (balance > 1 and value < node.left.key):
            print(f"Cây bị lệch trái - trái khi thêm nút: ({value})")
            
            # Lệch trái -> Xoay phải
            return self.right_rotate(node)
        
        #? TH2: lệch phải - phải
        if (balance < -1 and value > node.right.key):
            print(f"Cây bị lệch phải - phải khi thêm nút: ({value})")

            # Lệch phải -> Xoay trái
            return self.left_rotate(node)
        
        #? TH3: lệch trái - phải
        if (balance > 1 and value > node.left.key):
            print(f"Cây bị lệch phải - phải khi thêm nút: ({value})")

            # B1 -> Xoay trái nút gần kề
            node.left = self.left_rotate(node.left)
            
            # B2 -> Xoay phải nút bị lệch
            return self.right_rotate(node)

        
        #? TH4: lệch phải - trái
        if (balance < -1 and value < node.right.key):
            print(f"Cây bị lệch phải - trái khi thêm nút: ({value})")

            # B1 -> Xoay phải nút gần kề
            node.right = self.right_rotate(node.right)
            
            # B2 -> Xoay trái nút bị lệch
            return self.left_rotate(node)
        
        return node
    
    def search(self, search_value):
        result = self._search_recursive(self.root, search_value)
        
        if result:
            print(f"Đã tìm thấy giá trị: {search_value}")
        else:
            print("Giá trị không tồn tại!!!")
    
    def _search_recursive(self, node, search_value):    
        # Kiểm tra nếu không tìm thấy được nút:
        if node is None:
            return None
        
        # Kiểm tra giá trị tìm kiếm
        if search_value == node.key:
            return node
        else:
            if search_value < node.key:
                self._search_recursive(node.left, search_value)
            else:
                self._search_recursive(node.right, search_value)
        
    """
    PHƯƠNG THỨC IN CÂY
    """    
    def print_tree(self, node):
        if node is None:
            return None
        
        return {
            "key": node.key,
            "left": self.print_tree(node.left),
            "right": self.print_tree(node.right),
            "height": node.height
        }
        
        
class HashTable:
    def __init__(self, size):
        self.size = size

        # Mỗi key mình sẽ chứa 1 list con -> List comprehension
        self.table = [ [] for _ in range(size) ] # size = 10 -> table = [ [], [], [] ..., [] 10th ]
        # self.table = [ AVLTree() for _ in range(size)] # size = 10 -> table = [ tree1, tree2, ..., tree10 ]
                
    """
    PHƯƠNG THỨC BĂM DỮ LIỆU 
    """
    def hash_function(self, value):
        return value % self.size
    
    def hash_function_name(self, name):
        # ascii -> ordinal 
        return sum(ord(c) for c in name) % self.size
    
    def hash_function_2(self, value, hash_value):
        return (value + hash_value) % self.size
    
    def hash_function_name_2(self, name, hash_value):
        # ascii -> ordinal 
        return (sum(ord(c) for c in name) + hash_value) % self.size
    
    """
    PHƯƠNG THỨC THÊM (INSERT) DỮ LIỆU 
    """
    def insert(self, value):
        hash_value = self.hash_function(value)
        
        # Mảng -> kiểm tra chiều dài của mảng, Tree -> kiểm tra root có bị rỗng
        # if self.table[hash_value].root is None:
        #     self.table[hash_value].insert(value)

        if len(self.table[hash_value]) == 0:
            self.table[hash_value].append(value)
        else:
            # Open addressing 1 -> Tìm vị trí index còn trống trước
            for i in range(self.size):
                # if self.table[i].root is None:
                #     self.table[i].insert(value)
                #     return
                if len(self.table[i]) == 0:
                    self.table[i].append(value)
                    return
            
            # Open Addressing 2 -> tìm vị trí index mới để thêm vào
            new_hash_value = self.hash_function_2(value, hash_value)
            # self.table[new_hash_value].insert(value)
            self.table[new_hash_value].append(value)
            
    def insert_object(self, product):
        hash_value = self.hash_function_name(product["name"])
        
        # Mảng -> kiểm tra chiều dài của mảng, Tree -> kiểm tra root có bị rỗng
        # if self.table[hash_value].root is None:
        #     self.table[hash_value].insert(value)

        if len(self.table[hash_value]) == 0:
            self.table[hash_value].append(product)
        else:
            # Open addressing 1 -> Tìm vị trí index còn trống trước
            for i in range(self.size):
                # if self.table[i].root is None:
                #     self.table[i].insert(value)
                #     return
                if len(self.table[i]) == 0:
                    self.table[i].append(product)
                    return
            
            # Open Addressing 2 -> tìm vị trí index mới để thêm vào
            new_hash_value = self.hash_function_name_2(product["name"], hash_value)
            # self.table[new_hash_value].insert(value)
            self.table[new_hash_value].append(product)
        
    """
    PHƯƠNG THỨC TÌM KIẾM (SEARCH) DỮ LIỆU 
    """
    def search(self, value):
        hash_value = self.hash_function(value)
    
        for num in self.table[hash_value]:
            if num == value:
                print(f"Tìm thấy dữ liệu: ({value})")
                return
        
        print(f"Không tìm thấy dữ liệu: ({value})")
        
        # self.table[hash_value].search(value)
        
    def print_table(self):
        for i in range(self.size):
            print(f"key {i}: {json.dumps(self.table[i], indent=4)}")
    
    def print_tree(self):
        for i in range(self.size):
            print(f"key {i}: {json.dumps(self.table[i].print_tree(self.table[i].root), indent = 4)}")
        
hash_table = HashTable(6)

# numbers = [2, 7, 8, 9, 14, 20, 26]

# with open('data.json', "r") as file:
#     products = json.load(file) # chuyển JSON -> mảng
    

products = [
    {
        "id": 582875268,
        "name": "Sony Xperia 4061049",
        "price": 44193564,
        "category": "House"
    },
    {
        "id": 708927122,
        "name": "Eggs 837236",
        "price": 49315706,
        "category": "Bike"
    },
    {
        "id": 261869748,
        "name": "Nokia 429168",
        "price": 9868224,
        "category": "Watch"
    },
    {
        "id": 323782184,
        "name": "OnePlus 2642512",
        "price": 7477747,
        "category": "Beauty"
    },
    {
        "id": 730608594,
        "name": "Apple iPhone 2025919",
        "price": 17682692,
        "category": "House"
    },
    {
        "id": 466075644,
        "name": "Nokia 4481045",
        "price": 5241247,
        "category": "Food"
    },
    {
        "id": 69513903,
        "name": "Google Pixel 2250542",
        "price": 13447941,
        "category": "House"
    },
]

for p in products:
    hash_table.insert_object(p)
    hash_table.print_table()
    print("--------------------\n")

# for num in numbers:
#     hash_table.insert(num)
#     hash_table.print_table()
#     # hash_table.print_tree()
#     print("--------------------\n")