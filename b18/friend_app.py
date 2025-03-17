import json

class User:
    def __init__(self, id, fullName, age, email):
        self.id = id
        self.fullName = fullName
        self.age = age
        self.email = email

class Graph:
    #? Khởi tạo bằng Hash Table
    def __init__(self):
        self.users = {}
        self.friends = {}
        
    """PHƯƠNG THỨC THÊM NGƯỜI DÙNG (VERTEX)
    """
    def add_user(self, user):
        self.users[user.id] = user # chứa object người dùng tại key "id" của người dùng
        
        if user.id not in self.friends:
            self.friends[user.id] = set()
    
    """PHƯƠNG THỨC KIỂM TRA NGƯỜI DÙNG CÓ TỒN TẠI TRONG ĐỒ THỊ 
    """
    def validate_user(self, user_id):
        if user_id not in self.friends:
            print("Người dùng không tồn tại trong ứng dụng!")
            return False

        return True
            
    """PHƯƠNG THỨC KẾT BẠN (THÊM CẠNH - EDGE)
    
    #? vertex1: vị trí nút bắt đầu
    #? vertex2: vị trí nút kết thúc
    
    """
    def add_friend(self, user_id_1, user_id_2):
        if self.validate_user(user_id_1) and self.validate_user(user_id_2):     
            self.friends[user_id_1].add(user_id_2)
            self.friends[user_id_2].add(user_id_1)
            
    """PHƯƠNG THỨC HUỶ KẾT BẠN (XOÁ EDGE)
    
    #? vertex1: vị trí nút bắt đầu
    #? vertex2: vị trí nút kết thúc
    
    """
    def remove_friend(self, user_id_1, user_id_2):
        if self.validate_user(user_id_1) and self.validate_user(user_id_2):     
            
            # Kiểm tra 2 users có phải là bạn hay không
            if user_id_2 in self.friends[user_id_1]:
                self.friends[user_id_1].remove(user_id_2)
            
            if user_id_1 in self.friends[user_id_2]:
                self.friends[user_id_2].remove(user_id_1)
    
    """PHƯƠNG THỨC TÌM NÚT KỀ VỚI NÚT ĐANG ĐỨNG (GET NEIGHBOR)
    """
    def get_friends(self, user_id):
        if self.validate_user(user_id):
            id_list = self.friends[user_id]
            friend_list = []
            
            for id in id_list:
                friend = self.users[id]
                friend_list.append(friend)
                
            return friend_list
    
    """PHƯƠNG THỨC GỢI Ý KẾT BẠN (SUGGEST NEIGHBOR)
    """
    def suggest_friends(self, user_id):
        if not self.validate_user(user_id):
            return {}
        
        # C1: dùng vòng lặp for
        id_list = self.friends[user_id]
        suggest_id_list = set()
        
        for user_friend_id in id_list:
            for suggest_friend_id in self.friends[user_friend_id]:
                #! Điều kiện kiểm tra người dùng: 1 - k phải user, 2 - k phải bạn user
                if suggest_friend_id != user_id and suggest_friend_id not in id_list:
                    suggest_id_list.add(suggest_friend_id)
        
        suggest_friends = []
        
        for id in suggest_id_list:
            friend = self.users[id]
            suggest_friends.append(friend)
            
        return suggest_friends
        
    def __str__(self):
        return f"Friends: {self.friends}"
    
data = [
    {
        "id": 1,
        "fullName": "Nguyen Anh Duy",
        "age": 22,
        "email": "duy@email.com",
    },
    {
        "id": 2,
        "fullName": "Tran Van A",
        "age": 12,
        "email": "vana@email.com",
    },
    {
        "id": 3,
        "fullName": "Le Trong Hoang",
        "age": 34,
        "email": "hoang@email.com",
    },
    {
        "id": 4,
        "fullName": "Ho Van H",
        "age": 50,
        "email": "h@email.com",
    },
    {
        "id": 5,
        "fullName": "Chi Thien Lam",
        "age": 10,
        "email": "lam@email.com",
    }
]

graph = Graph()

for d in data:
    user = User(**d) # destructuring
    graph.add_user(user)
    
graph.add_friend(1, 2)
graph.add_friend(2, 3)
graph.add_friend(2, 5)
graph.add_friend(4, 5)

print(graph)

# for user in graph.get_friends(2):
#     print(user.fullName)

suggest_id = int(input("Enter suggested friend id: "))

for user in graph.suggest_friends(suggest_id):
    print(f"{user.id}: {user.fullName}")


