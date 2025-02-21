import customtkinter as ctk

# tạo class LearningOOP
class LearningOOP(ctk.CTk):
    # hàm khởi tạo
    def __init__(self):
        # gọi hàm khởi tạo của class cha
        super().__init__()

        # setup width and height
        self.geometry("800x900")

        # setup title
        self.title("Learning customtkinter")

        # gọi hàm design layout
        self.create_layout()

    def get_value(self, choice):
        print("Bạn đã chọn: ", choice)

    # hàm design layout
    def create_layout(self):
        # tạo button
        # button = ctk.CTkButton(app, text="Button", width=150, height=50, corner_radius=10, fg_color="red")
        self.button = ctk.CTkButton(self, text="Button", width=150, height=100, corner_radius=10, fg_color="red")
        self.button.pack(pady=10)

        # tạo option menu
        self.option_menu = ctk.CTkOptionMenu(self, values=["option 1", "option 2", "option 3"], command=self.get_value)
        self.option_menu.pack(pady=10)


if __name__ == "__main__":
    app = LearningOOP()
    # start app
    app.mainloop()