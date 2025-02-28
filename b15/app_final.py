import customtkinter # pip / pip3 install customtkinter
import os 
from PIL import Image, ImageDraw, ImageOps # pip install pillow
import json
from phone_tree import AVLTree

#TODO 1: Tạo Product Frame
class Product(customtkinter.CTkFrame):
    # Tạo border-radius (độ cong của viền) cho ảnh
    def add_border_radius(self, image_path, radius):
        image = Image.open(image_path)
        mask = Image.new('L', image.size, 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.rounded_rectangle([(0, 0), image.size], radius=radius, fill=255)
        result = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
        result.putalpha(mask)
        return result
    
    def buy_product(self):
        print(f"Mua sản phẩm {self.product["name"]} này giá: ${self.product["price"]}")
    
    def __init__(self, master, product):
        super().__init__(master=master, fg_color="black", corner_radius=10)
        self.product = product

        # Chia product_frame ra thành 2 phần trên dưới
        top_frame = customtkinter.CTkFrame(master=self, fg_color="black", corner_radius=10)
        top_frame.pack(expand=True, fill="both", pady=(10, 0)) # padding_top = 10, padding_bottom = 0

        bottom_frame = customtkinter.CTkFrame(master=self, fg_color="black", corner_radius=10)
        bottom_frame.pack(expand=True, fill="both", pady=(0, 10))

        #? Tạo khung chứa hình ảnh 
        image_path = os.path.join("img", product["image"])
        custom_image = self.add_border_radius(image_path=image_path, radius=20)
        # image = customtkinter.CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path), size=(180, 180))
        image = customtkinter.CTkImage(light_image=custom_image, dark_image=custom_image, size=(180, 180))

        # 1. Hình ảnh (image)
        image_frame = customtkinter.CTkLabel(master=top_frame, image=image, text="")
        image_frame.pack(padx=15)

        #? Tạo khung chứa thông tin sản phẩm
        info_frame = customtkinter.CTkFrame(master=bottom_frame, fg_color="black")
        info_frame.pack(pady=10, padx=0)

        # 2. Tên sản phẩm (name)
        name = customtkinter.CTkLabel(master=info_frame, font=customtkinter.CTkFont("Arial", 18, "bold"), text_color="orange", text=product["name"]) # màu sắc: tên màu, hex, rgb
        name.pack()

        # 3. Loại sản phẩm (category)
        category_frame = customtkinter.CTkFrame(master=info_frame, fg_color="pink", corner_radius=15)
        category_frame.pack()

        category = customtkinter.CTkLabel(master=category_frame, font=customtkinter.CTkFont("Arial", 11, "bold"), text_color="black", text=product["category"])
        category.pack(anchor="center", padx=10)

        # 4. Mô tả (description)
        description = customtkinter.CTkLabel(master=info_frame, text_color="white", text=product["description"])
        description.pack(pady=(5, 0))

        # 5. Giá sản phẩm (price)
        price = customtkinter.CTkLabel(master=info_frame, font=customtkinter.CTkFont("Helvetica", 15, "bold"), text_color="yellow", text=f"$ {product["price"]}")
        price.pack()

        # Nút mua sản phẩm
        button = customtkinter.CTkButton(info_frame, fg_color="darkblue", text="Mua", command=self.buy_product)
        button.pack(pady=(15, 0))
        
#TODO 2: Tạo ScrollView
class ScrollView(customtkinter.CTkScrollableFrame):
    def __init__(self, master, product_list):
        super().__init__(master=master)

        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        for i in range(len(product_list)):
            product_frame = Product(master=self, product=product_list[i])
            product_frame.grid(column = i % 4, row = i // 4, sticky="nesw", padx=(0, 10), pady=(0, 10)) 

#TODO 3: Tạo Header
class Header(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, fg_color="black", corner_radius=0)

        self.entry_min = customtkinter.CTkEntry(master=self, placeholder_text="Nhập giá thấp nhất")
        self.entry_min.pack(side="left", padx=(10,0))

        self.entry_max = customtkinter.CTkEntry(master=self, placeholder_text="Nhập giá cao nhất")
        self.entry_max.pack(side="left", padx=(10,0))

        search_button = customtkinter.CTkButton(self, fg_color="green", text="Mua", width=200, command=master.filter)
        search_button.pack(side="left", padx=(25,0))

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        #? Cấu hình màu sắc mặc định của window
        customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
        customtkinter.set_appearance_mode("light") # system (default), light, dark

        #? Cấu hình ứng dụng: tiêu đề, kích thước window, khả năng thay đổi tỉ lệ màn hình
        self.title("Phone Shop")
        self.geometry("1100x800") #1024x720
        self.resizable(True, False) # 1. width, 2. height
        
        self.products = self.get_data()
        
        self.avl_data = AVLTree()
        
        # Thêm sản phẩm vào cây AVL
        for product in self.products:
            self.avl_data.insert(product)
        
        #? Khởi tạo Header
        self.header_frame = Header(master=self)
        self.header_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        
        #? Khởi tạo ScrollView
        self.scroll_frame = ScrollView(master=self, product_list=self.products)
        self.scroll_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.9) 
        
    def get_data(self):
        products = []

        with open(os.path.join("data", "data.json"), "r", encoding="utf-8") as file:
            products = json.load(file)
            
            for product in products:
                print(product)   
                
        return products
    
    def filter(self):
        min_price = self.header_frame.entry_min.get()
        max_price = self.header_frame.entry_max.get()
        
        if min_price is None or max_price is None:
            return None
        
        data_search = self.avl_data.find_phones(self.avl_data.root, min_price=int(min_price), max_price=int(max_price))
        
        print(json.dumps(data_search, indent=4))
        
        #! C1: research -> xoá frame cũ thay frame mới
        #* C2: tạo 1 frame mới và ghi đè lên frame cũ
        new_scroll_frame = ScrollView(master=self, product_list=data_search)
        new_scroll_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.9) 
        
app = App()

app.mainloop()
