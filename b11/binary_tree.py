class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # Khi chưa có nút rễ -> mình sẽ gán giá trị của nút rễ là 1 node mới
        if self.root == None:
            self.root = Node(key = value)
        else:
            self.root = self._insert_recursive(self.root, value)
            
        # print(f"Thêm thành công {value}")
        
    def _insert_recursive(self, node, value):
        if value < node.key:
            #! Khi chưa có nút con bên trái
            if node.left == None:
                node.left = Node(key=value)
            else: #* Khi đã có nút con bên trái rồi 
                self._insert_recursive(node.left, value)
        else:
            #! Khi chưa có nút con bên phải
            if node.right == None:
                node.right = Node(key=value)
            else: #* Khi đã có nút con bên phải rồi
                self._insert_recursive(node.right, value)
                
    
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
    PHƯƠNG THỨC XOÁ 
    @param
    + key: gía trị muốn xoá
    """
    def delete(self, key):
        """Xóa một phần tử trong BST"""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node  # Không tìm thấy giá trị, trả về chính nó

        # Tìm nút cần xóa
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Trường hợp 1: Nút không có con hoặc chỉ có một con
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Trường hợp 2: Nút có hai con
            # Tìm Inorder Successor (nút nhỏ nhất trong cây con phải)
            min_larger_node = self._min_value_node(node.right)
            node.key = min_larger_node.key  # Gán giá trị mới
            node.right = self._delete_recursive(node.right, min_larger_node.key)  # Xóa nút thay thế

        return node

    def _min_value_node(self, node):
        """Tìm nút có giá trị nhỏ nhất trong cây con phải"""
        while node.left:
            node = node.left
        return node
    
    """
    PHƯƠNG THỨC DUYỆT CÂY 
    @param
    + type: (1, 2, 3 tương ứng với các thứ tự duyệt cây)
    """
    def traverse(self, type):
        if type == 1: # 1 - preorder
            self.preorder(self.root)
        elif type == 2: # 2 - inorder
            self.inorder(self.root)
        elif type == 3: # 3 - postorder
            self.postorder(self.root)
        
    """PREORDER
    Nút hiện tại (gốc) -> Nút trái -> Nút phải
    """
    def preorder(self, node):
        # result = ""
        
        if node:
            print(node.key, end=" -> ")
            # result += f"{node.key} ->" 
            self.preorder(node.left)
            self.preorder(node.right)
        
        # diff = len(result) - 3
            
        # result = str[:diff]
        # return result
        
    """INORDER
    Nút trái -> Nút hiện tại (gốc) -> Nút phải
    """
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" -> ")
            self.inorder(node.right)   
        
    """POSTORDER
    Nút trái -> Nút phải -> Nút hiện tại (gốc)
    """
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=" -> ")


#TODO: KHỞI TẠO BINARY TREE
binary_tree = BinaryTree()

numbers = [13, 20, 4, 2, 16, 14, 22, 5, 8]

for num in numbers:
    binary_tree.insert(num)

#TODO: DUYỆT CÂY
print("1. Preorder: ")
print(binary_tree.traverse(1))
    
# print("2. Inorder: ")
# print(binary_tree.traverse(2))

# print("3. Postorder: ")
# print(binary_tree.traverse(3))

#TODO: TÌM KIẾM GIÁ TRỊ TRONG CÂY NHỊ PHÂN
binary_tree.search(50)

# print(binary_tree.preorder(binary_tree.root.right))