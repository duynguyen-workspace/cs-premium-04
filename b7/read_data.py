import json

with open("tiki_data.json", "r") as file:
    
    read_data = json.load(file) # chuyển JSON -> mảng
    
    print(f"Số dòng trong file tiki_data.json: {len(file.readlines())}")
    print(f"Số lượng sản phẩm: {len(read_data)}")