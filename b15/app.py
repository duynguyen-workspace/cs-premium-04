import customtkinter # pip / pip3 install customtkinter
import os 
from PIL import Image, ImageDraw, ImageOps # pip install pillow
import json
from phone_tree import AVLTree

#? Khởi tạo ứng dụng customtkinter
app = customtkinter.CTk()

#? Cấu hình màu sắc mặc định của window
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_appearance_mode("light") # system (default), light, dark

#? Cấu hình ứng dụng: tiêu đề, kích thước window, khả năng thay đổi tỉ lệ màn hình
app.title("Phone Shop")
app.geometry("1100x800") #1024x720
app.resizable(True, False) # 1. width, 2. height

def buy_product(product):
    print(f"Mua sản phẩm {product["name"]} này giá: ${product["price"]}")

"""
HÀM LỌC SẢN PHẨM THEO GIÁ TIỀN
"""
def filter():
    min_price = entry_min.get()
    max_price = entry_max.get()
    
    if min_price is None or max_price is None:
        return None
    
    data_search = avl_data.find_phones(avl_data.root, min_price=int(min_price), max_price=int(max_price))
    
    print(json.dumps(data_search, indent=4))
    
    #! C1: research -> xoá frame cũ thay frame mới
    #* C2: tạo 1 frame mới và ghi đè lên frame cũ
    new_scroll_frame = customtkinter.CTkScrollableFrame(master=app)
    new_scroll_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.9) 
    new_scroll_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)  
    
    for i in range(len(data_search)):
        #TODO 1: Tạo Product Frame
        product_frame = customtkinter.CTkFrame(master=new_scroll_frame, fg_color="black", corner_radius=10) # foreground
        product_frame.grid(column = i % 4, row = i // 4, sticky="nesw", padx=(0, 10), pady=(0, 10)) 

        # Chia product_frame ra thành 2 phần trên dưới
        top_frame = customtkinter.CTkFrame(master=product_frame, fg_color="black", corner_radius=10)
        top_frame.pack(expand=True, fill="both", pady=(10, 0)) # padding_top = 10, padding_bottom = 0

        bottom_frame = customtkinter.CTkFrame(master=product_frame, fg_color="black", corner_radius=10)
        bottom_frame.pack(expand=True, fill="both", pady=(0, 10))

        # Tạo border-radius (độ cong của viền) cho ảnh
        def add_border_radius(image_path, radius):
            image = Image.open(image_path)
            mask = Image.new('L', image.size, 0)
            mask_draw = ImageDraw.Draw(mask)
            mask_draw.rounded_rectangle([(0, 0), image.size], radius=radius, fill=255)
            result = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
            result.putalpha(mask)
            return result

        #? Tạo khung chứa hình ảnh 
        image_path = os.path.join("img", data_search[i]["image"])
        custom_image = add_border_radius(image_path=image_path, radius=20)
        # image = customtkinter.CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path), size=(180, 180))
        image = customtkinter.CTkImage(light_image=custom_image, dark_image=custom_image, size=(180, 180))

        # 1. Hình ảnh (image)
        image_frame = customtkinter.CTkLabel(master=top_frame, image=image, text="")
        image_frame.pack(padx=15)

        #? Tạo khung chứa thông tin sản phẩm
        info_frame = customtkinter.CTkFrame(master=bottom_frame, fg_color="black")
        info_frame.pack(pady=10, padx=0)

        # 2. Tên sản phẩm (name)
        name = customtkinter.CTkLabel(master=info_frame, font=customtkinter.CTkFont("Arial", 18, "bold"), text_color="orange", text=data_search[i]["name"]) # màu sắc: tên màu, hex, rgb
        name.pack()

        # 3. Loại sản phẩm (category)
        category_frame = customtkinter.CTkFrame(master=info_frame, fg_color="pink", corner_radius=15)
        category_frame.pack()

        category = customtkinter.CTkLabel(master=category_frame, font=customtkinter.CTkFont("Arial", 11, "bold"), text_color="black", text=data_search[i]["category"])
        category.pack(anchor="center", padx=10)

        # 4. Mô tả (description)
        description = customtkinter.CTkLabel(master=info_frame, text_color="white", text=data_search[i]["description"])
        description.pack(pady=(5, 0))

        # 5. Giá sản phẩm (price)
        price = customtkinter.CTkLabel(master=info_frame, font=customtkinter.CTkFont("Helvetica", 15, "bold"), text_color="yellow", text=f"$ {data_search[i]["price"]}")
        price.pack()

        # Nút mua sản phẩm
        button = customtkinter.CTkButton(info_frame, fg_color="darkblue", text="Mua", command=buy_product(data_search[i]))
        button.pack(pady=(15, 0))
    

#TODO 3: Tạo Header
header_frame = customtkinter.CTkFrame(master=app, fg_color="black", corner_radius=0)
header_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1)

entry_min = customtkinter.CTkEntry(master=header_frame, placeholder_text="Nhập giá thấp nhất")
entry_min.pack(side="left", padx=(10,0))

entry_max = customtkinter.CTkEntry(master=header_frame, placeholder_text="Nhập giá cao nhất")
entry_max.pack(side="left", padx=(10,0))

search_button = customtkinter.CTkButton(header_frame, fg_color="green", text="Mua", width=200, command=filter)
search_button.pack(side="left", padx=(25,0))

#TODO 2: Tạo ScrollView
scroll_frame = customtkinter.CTkScrollableFrame(master=app)
scroll_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.9) 
scroll_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

#TODO 4: Load danh sách sản phẩm
products = []

with open(os.path.join("data", "data.json"), "r", encoding="utf-8") as file:
    products = json.load(file)
    
    for product in products:
        print(product)
        
avl_data = AVLTree()

for product in products:
    # Thêm sản phẩm vào cây AVL
    avl_data.insert(product)

# Vòng lặp mình tạo n sản phẩm
for i in range(len(products)): # 0
    
    #TODO 1: Tạo Product Frame
    product_frame = customtkinter.CTkFrame(master=scroll_frame, fg_color="black", corner_radius=10) # foreground
    product_frame.grid(column = i % 4, row = i // 4, sticky="nesw", padx=(0, 10), pady=(0, 10)) 

    # Chia product_frame ra thành 2 phần trên dưới
    top_frame = customtkinter.CTkFrame(master=product_frame, fg_color="black", corner_radius=10)
    top_frame.pack(expand=True, fill="both", pady=(10, 0)) # padding_top = 10, padding_bottom = 0

    bottom_frame = customtkinter.CTkFrame(master=product_frame, fg_color="black", corner_radius=10)
    bottom_frame.pack(expand=True, fill="both", pady=(0, 10))

    # Tạo border-radius (độ cong của viền) cho ảnh
    def add_border_radius(image_path, radius):
        image = Image.open(image_path)
        mask = Image.new('L', image.size, 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.rounded_rectangle([(0, 0), image.size], radius=radius, fill=255)
        result = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
        result.putalpha(mask)
        return result

    #? Tạo khung chứa hình ảnh 
    image_path = os.path.join("img", products[i]["image"])
    custom_image = add_border_radius(image_path=image_path, radius=20)
    # image = customtkinter.CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path), size=(180, 180))
    image = customtkinter.CTkImage(light_image=custom_image, dark_image=custom_image, size=(180, 180))

    # 1. Hình ảnh (image)
    image_frame = customtkinter.CTkLabel(master=top_frame, image=image, text="")
    image_frame.pack(padx=15)

    #? Tạo khung chứa thông tin sản phẩm
    info_frame = customtkinter.CTkFrame(master=bottom_frame, fg_color="black")
    info_frame.pack(pady=10, padx=0)

    # 2. Tên sản phẩm (name)
    name = customtkinter.CTkLabel(master=info_frame, font=customtkinter.CTkFont("Arial", 18, "bold"), text_color="orange", text=products[i]["name"]) # màu sắc: tên màu, hex, rgb
    name.pack()

    # 3. Loại sản phẩm (category)
    category_frame = customtkinter.CTkFrame(master=info_frame, fg_color="pink", corner_radius=15)
    category_frame.pack()

    category = customtkinter.CTkLabel(master=category_frame, font=customtkinter.CTkFont("Arial", 11, "bold"), text_color="black", text=products[i]["category"])
    category.pack(anchor="center", padx=10)

    # 4. Mô tả (description)
    description = customtkinter.CTkLabel(master=info_frame, text_color="white", text=products[i]["description"])
    description.pack(pady=(5, 0))

    # 5. Giá sản phẩm (price)
    price = customtkinter.CTkLabel(master=info_frame, font=customtkinter.CTkFont("Helvetica", 15, "bold"), text_color="yellow", text=f"$ {products[i]["price"]}")
    price.pack()

    # Nút mua sản phẩm
    button = customtkinter.CTkButton(info_frame, fg_color="darkblue", text="Mua", command=buy_product(products[i]))
    
    button.pack(pady=(15, 0))

app.mainloop()

