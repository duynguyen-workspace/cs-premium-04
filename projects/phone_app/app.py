import customtkinter
import os
import json
from PIL import Image, ImageDraw, ImageOps

from BSTree import find_phone, insert

def add_border_radius(image_path, radius):
    image = Image.open(image_path)
    mask = Image.new('L', image.size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([(0, 0), image.size], radius=radius, fill=255)
    result = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    result.putalpha(mask)
    return result

# Product Frame class
class ProductFrame(customtkinter.CTkFrame):
    def __init__(self, master, product):
        super().__init__(master=master, fg_color="black", corner_radius=15)
        
        top_frame = customtkinter.CTkFrame(master=self, fg_color="black", corner_radius=15)
        top_frame.pack(expand=True, fill="y", anchor="center")
        
        bottom_frame = customtkinter.CTkFrame(master=self, fg_color="black", corner_radius=15)
        bottom_frame.pack(expand=True, fill="y", anchor="center")
        
        # Setup image frame
        image_path = os.path.join("img",product["img"])
        image = customtkinter.CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path), size=(180, 180))
        img_frame = customtkinter.CTkLabel(master=top_frame, image=image, text="")
        img_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Setup information frame
        info_frame = customtkinter.CTkFrame(master=bottom_frame, fg_color="black")
        info_frame.pack(expand=True, fill="both", anchor="center", pady=(0, 20))
        
        product_name = customtkinter.CTkLabel(info_frame, text=product["name"], text_color="white")
        product_price = customtkinter.CTkLabel(info_frame, text="$ {}".format(product["price"]), text_color="white")
        button = customtkinter.CTkButton(info_frame, text="Buy Now", fg_color="blue", width=120)
        
        product_name.pack()
        product_price.pack()
        button.pack(pady=(10, 0))
        
        # Setup image
        rounded_image = add_border_radius(image_path, 10)
        image = customtkinter.CTkImage(light_image=rounded_image, dark_image=rounded_image, size=(20, 20))
        # label = customtkinter.CTkLabel(master=frame, image=image)
        # label.pack(expand=True, fill="both")


# Initialise Product List class
class ProductListScrollBar(customtkinter.CTkScrollableFrame):
    def __init__(self, master, product_list):
        super().__init__(master=master)
        self.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        
        # Iterate through product_list and create product frames according to data
        for i in range(len(product_list)):
            product_frame = ProductFrame(self, product=product_list[i])
            product_frame.grid(column=i % 4, row=i // 4, sticky="nesw", padx=5, pady=5)
            
class Header(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, fg_color="white")
        
        top_frame = customtkinter.CTkFrame(master=self, fg_color="white")
        top_frame.pack(side="top", expand=True, fill="x", anchor="center", padx=50)
        
        bottom_frame = customtkinter.CTkFrame(master=self, fg_color="white")
        bottom_frame.pack(side="bottom", expand=True, fill="x", anchor="center", padx=50)
        
        # load input min và max price
        self.entryMin = customtkinter.CTkEntry(master=top_frame, placeholder_text="Price min")
        self.entryMin.pack(side="left", expand=True, fill="x", padx=(0, 10))

        self.entryMax = customtkinter.CTkEntry(master=top_frame, placeholder_text="Price max")
        self.entryMax.pack(side="left", expand=True, fill="x", padx=(10, 0))
        
        self.searchButton = customtkinter.CTkButton(master=bottom_frame, text="Search Products", fg_color="green", command=master.search_phone)
        self.searchButton.pack(side="left", expand=True, fill="x")


class App(customtkinter.CTk):
    def __init__(self, product_list):
        # Initialise App
        super().__init__()
        
        # Configure theme and appearance mode
        customtkinter.set_default_color_theme("green")
        customtkinter.set_appearance_mode("System")
        
        # Configure title and window size
        self.title("Phone Shop")
        self.geometry("1024x700")
        
        # Configure grid columns and rows template
        self.columnconfigure((0), weight=1)
        self.rowconfigure((0), weight=1)
        
        # Configure window resizable status
        self.resizable(width=True, height=False)
        
        # Load header
        self.header = Header(master=self)
        self.header.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        
        # Load khung chứa danh sách sản phẩm
        self.frameScrollBar = ProductListScrollBar(self, product_list=product_list)
        self.frameScrollBar.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.frameScrollBar.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)
        
        # Load binary search tree data
        self.bstData = None
        
        for item in product_list:
            self.bstData = insert(self.bstData, item)
        
    def search_phone(self):
        min_price = int(self.header.entryMin.get())
        max_price = int(self.header.entryMax.get())
        
        if min_price is None or max_price is None:
            return self.product_list
        
        data_search = find_phone(self.bstData, min_price, max_price)
        
        print(data_search)
        
        self.frameScrollBar = ProductListScrollBar(self, product_list=data_search)
        self.frameScrollBar.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.frameScrollBar.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

# -----MAIN PROGRAM-----        

# Get product data
products = []
with open(os.path.join("data", "data.json"), "r", encoding="utf-8") as file:
    products = json.load(file)
    
    for product in products:
        print(product)

# Create app instance
app = App(product_list=products)
app.mainloop()