'''
HƯỚNG DẪN CÀO DỮ LIỆU (CRAWL DATA) BẰNG PYTHON
'''

#? B1: cài đặt thư viện requests 
# pip3 install requests (MAC) OR p
# ip install requests (WINDOW)

# pip install random 
# pip install time
import requests
import json
import random
import time

'''
* FIX LỖI KHÔNG CHẠY ĐƯỢC TRÊN WINDOWS *:
import sys
sys.stdout.reconfigure(encoding='utf-8')
'''

#? B2: copy url, headers và params từ tiki.vn

# query string / query param:

# C1: url = "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&is_mweb=1&aggregations=2&version=home-persionalized&_v=&trackity_id=9910f7f4-4ee4-00c0-9a7a-636f88e1ccd3&category=1801&page=4"

url = "https://tiki.vn/api/personalish/v1/blocks/listings" 

# headers
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36"
}

# params
params = {
    "limit": 40,
    "include": "advertisement",
    "is_mweb": 1,
    "aggregations": 2,
    "version": "home-persionalized",
    "_v": "",
    "trackity_id": "9910f7f4-4ee4-00c0-9a7a-636f88e1ccd3",
    "category": 1801,
    "page": 1
}

# TODO: BÀI TẬP 1 - Lấy dữ liệu của 1 danh mục, lấy từ trang số 1 -> n
pages = 20

# TODO: BÀI TẬP 2: lấy dữ liệu của 5 danh mục (mỗi danh mục lấy khoảng 5 trang), lấy đến khi nào file json có khoảng 3000 dữ liệu
category_list = [2549, 1801, 1, 8322, 1975, 1686]

product_list = []

for category in category_list:
    if len(product_list) >= 3000: #! nếu tới 3000 sản phẩm -> dừng vòng lặp
        print("Dừng cào dữ liệu tại category!!!")
        break
    
    params["category"] = category # lặp các id category khác nhau
    
    print(f"* Đang lấy dữ liệu của category - {category}... *")

    for i in range(pages): # 0 -> 5
        if len(product_list) >= 3000: #! nếu tới 3000 sản phẩm -> dừng vòng lặp
            print("Dừng cào dữ liệu tại trang!!!")
            break
        
        params["page"] = i + 1

        #? B2: Gọi API tiki lấy dữ liệu 
        response = requests.get(url, headers=headers, params=params) # C1: response = requests.get(url, headers=headers)

        # print(f"Response: {response.json().get('data')[5]}")
        
        print(f"Lấy dữ liệu thành công từ trang - {i + 1}!")

        data = response.json().get("data")

        #? B3: Lấy toàn bộ dữ liệu trong mảng
        
        for index, item in enumerate(data):
            
            # Tạo 1 object mới chứa thông tin sản phẩm 
            product_item = {
                "id": item.get("id"),
                "product_name": item.get("name"),
                "price": item.get("price"),
                "brand": item.get("brand_name"),
                "discount": item.get("discount"),
                "rating": item.get("rating_average"),
                "thumbnail_url": item.get("thumbnail_url"),
                "quantity_sold": item.get("quantity_sold")
            }
            
            product_list.append(product_item)
            
            # print(f"Item {index + 1}: {product_item}\n")
        
        
        #? Delay quá trình gọi API
        delay = random.randrange(5, 11) # delay: 5s -> 10s
        
        print(f"--- Dừng cào dữ liệu trong {delay}s. ---")
        time.sleep(delay)

#? B5: Ghi dữ liệu cào được vào file json
with open("tiki_data.json", "w", encoding="utf-8") as file:
    json.dump(product_list, file, ensure_ascii = False, indent = 4) # Chuyển object của mảng -> JSON

print("Ghi file thành công!")

# cd: change directory



