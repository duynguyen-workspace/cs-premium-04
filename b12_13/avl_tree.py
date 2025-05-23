import json

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
        
avl_tree = AVLTree()

# numbers = [1, 2, 3, 4, 5, 6, 23, 26, 21, 20, 11]
characters = ["A", "A" "B", "C", "D", "E", "F", "W", "Z", "U", "T", "K", "I"]


# for num in numbers:
#     avl_tree.insert(num)
#     print(json.dumps(avl_tree.print_tree(avl_tree.root), indent = 4))

for c in characters:
    avl_tree.insert(c)
    print(json.dumps(avl_tree.print_tree(avl_tree.root), indent = 4))
    