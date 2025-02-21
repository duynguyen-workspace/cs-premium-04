# import lib customtkinter
import customtkinter as ctk

# create a window
app = ctk.CTk()
# setup width and height
app.geometry("800x900")

# disable resize window
app.resizable(False, False)


# setup title
app.title("Learning customtkinter")

# 1. example về button
button = ctk.CTkButton(app, text="Button", width=150, height=50, corner_radius=10, fg_color="red")
#pad: padding: khoảng cách giữa các phần tu, component
#padx: padding theo chiều ngang
#pady: padding theo chiều dọc
# default: vị trí của component này sẽ nằm ở vị trí top
# button.pack(pady=10, padx=10)
button.grid(row=0, column=0)
# 2. example về label
label = ctk.CTkLabel(app, text="Label", width=200, height=100, fg_color="green", corner_radius=10, font=("Arial", 20))
# label.pack(pady=20)
label.grid(row=1, column=0)

#define function to get value from option menu
def get_value(value):
    print("Bạn đã chọn: ", value)

# 3. Example về option menu
option_menu = ctk.CTkOptionMenu(app, values=["option 1", "option 2", "option 3"], command=get_value)
# option_menu.pack(pady=10)

# start app
app.mainloop()

#VSCode: python3 learning.py