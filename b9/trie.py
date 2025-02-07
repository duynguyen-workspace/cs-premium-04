class TrieNode:
    def __init__(self):
        self.children = {} # khởi tạo 1 dictionary rỗng
        self.endWord = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    #? Phương thức thêm phần tử vào Trie 
    def insert(self, word):
        curr_node = self.root
        
        # Lặp qua từng kí tự có trong từ
        for char in word: # "cat" -> [c, a, t]
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]
            
        # Cập nhật thuộc tính xác định kết thúc từ
        curr_node.endWord = True
    
    #? Phương thức tìm kiếm -> trả về boolean
    def search(self, word):
        curr_node = self.root
        
        # Lặp qua từng kí tự có trong từ
        for char in word: # "cat" -> [c, a, t]
            if char not in curr_node.children:
                print("Từ không tồn tại trong Trie!")
                return False
            curr_node = curr_node.children[char]
        
        # Kiểm tra nếu từ đó tồn tại (endWord = True)
        print("Tìm thấy từ!") if curr_node.endWord == True else print("Không tìm thấy từ!")
        
        """_thay thế code trên_
        if curr_node.endWord == True:
            return True
        else: 
            return False
        """
        
    #? In cây Trie
    def print_tree(self):
        self._print_tree(self.root, "")
        
        
    def _print_tree(self, node, current_prefix):
        # Nếu từ đó tồn tại -> Xuất ra màn hình
        if node.endWord == True:
            print(current_prefix)
            
        # Truy xuất key và value của danh sách children: 
        for char, child_node in node.children.items(): # == for key, value in dictionary.items()
            self._print_tree(child_node, current_prefix + char)
            
    
    #? Phương thức kiểm tra từ bắt đầu bằng tiền tố được khai báo -> trả về vị trí nút đã duyệt qua tiền tố
    def start_with(self, prefix):
        curr_node = self.root
        
        for char in prefix:
            if char not in curr_node.children:
                return None
            curr_node = curr_node.children[char]
        
        return curr_node
    
    #? Phương thức tìm toàn bộ từ có tiền tố được khai báo
    def find_all_words(self, node, curr_prefix):
        
        # Tạo mảng chứa các từ có thể gợi ý
        suggested_words = []
        
        # Nếu tìm thấy từ tồn tại ở nút hiện tại -> thêm vào mảng
        if node.endWord == True:
            suggested_words.append(curr_prefix)
        
        # Cập nhật tiền tố mới và đệ quy lại phương thức (VD: gợi ý tiền tố "c" -> tìm các tiền tố "ca", "co", vv...)
        for char, child_node in node.children.items():
            suggested_words.extend(self.find_all_words(child_node, curr_prefix + char))
        
        print("Các từ gợi ý:", suggested_words)
        
        # Trả về kết quả của đệ quy
        return suggested_words
        
    #? Phương thức gợi ý -> chức năng auto-complete
    def auto_complete(self, prefix):
        
        # Lấy vị trí nút chứa tiền tố
        current = self.start_with(prefix)
        
        if current == None: #! Nếu tiền tố không tồn tại trong Trie -> xuất thông báo rỗng
            print("không có từ để gợi ý...")
        else: #* Nếu tiền tố tồn tại -> in danh sách các từ 
            self.find_all_words(self.start_with(prefix), prefix)
            

#TODO: khởi tạo cây Trie
trie = Trie()

#TODO: thêm các từ mới vào Trie
word_list = ["cat", "banana", "obama", "car", "cow", "alibaba", "bana"]

for word in word_list:
    trie.insert(word)

#TODO: in các từ có trong cây Trie
# trie.print_tree()

#TODO: tìm kiếm từ có trong cây Trie
# trie.search("cy")

#TODO: chức năng gợi ý từ
trie.auto_complete("c") # tham số: truyền vào 1 tiền tố


