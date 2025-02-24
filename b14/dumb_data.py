import json
import random

# Danh sách các tên mẫu
sample_names = [
    "Apple iPhone",
    "Samsung Galaxy",
    "Google Pixel",
    "OnePlus",
    "Xiaomi Redmi",
    "Teddy_Bear",
    "Sony Xperia",
    "LG G",
    "Nokia",
    "Eggs",
    "Doll",
    "Perfume",
    "Lipstick",
    "History_Book",
    "Bed"
]

sample_category = [
    "Phone",
    "Toy",
    "Fashion",
    "Watch",
    "Bike",
    "Shoe",
    "House",
    "Beauty",
    "Food",
    "School"
]

# Định nghĩa object mẫu
sample_object = {
    "id": 197216291,
    "name": "Apple iPhone 14 Pro Max",
    "price": 26450000,
    "category": ""
}

# Số lượng data bạn muốn tạo
num_data = 10

# List chứa các data mới
data_list = []

# Tạo các data mới
for _ in range(num_data):
    new_data = sample_object.copy()
    new_data["id"] = random.randint(1, 1000000000)  # Giá trị ngẫu nhiên cho id
    new_data["name"] = f"{random.choice(sample_names)} {random.randint(1, 5000000)}"

    new_data["price"] = random.randint(1000000, 50000000)  # Giá trị ngẫu nhiên cho price
    # Giá trị ngẫu nhiên cho original_price
    new_data["category"] =  f"{random.choice(sample_category)}"
    data_list.append(new_data)

# Đường dẫn đến file JSON để lưu dữ liệu
output_file_path = "data.json"

# Lưu dữ liệu vào file JSON
with open(output_file_path, "w") as output_file:
    json.dump(data_list, output_file, indent=4)

print(f"Dữ liệu đã được lưu vào file: {output_file_path}")
