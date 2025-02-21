import customtkinter as ctk

class StudentManager(ctk.CTk):
    def __init__(self):
        super().__init__()

        # define list student
        self.students = []

        self.geometry("900x600")
        self.title("Quản lý học sinh")

        # setup mode: dark, light
        ctk.set_appearance_mode("light")

        # create design_layout
        self.create_layout()

    def add_student(self):
        # get value from entry
        name = self.name_entry.get()
        age = self.age_entry.get()
        student_class = self.class_entry.get()

        # print("Name: ", name)
        # print("Age: ", age)
        # print("Class: ", student_class).0

        # show information student in listbox
        student_info = f"Tên: {name} - Tuổi: {age} - Lop: {student_class}"
        self.student_listbox.configure(state="normal")
        self.student_listbox.delete("1.0", "end")
        student = {
            "name": name,
            "age": age,
            "class": student_class
        }

        self.students.append(student)
        for stu in self.students:
            self.student_listbox.insert("end", f"Tên: {stu.get("name")}, Tuổi: {stu.get("age")}, Lớp: {stu.get("class")}\n")

        # self.student_listbox.insert("end", student_info + "\n")
        # self.student_listbox.configure(state="disabled")


    def create_layout(self):
        # create form frame
        self.form_frame = ctk.CTkFrame(self, corner_radius=10)
        self.form_frame.pack(side="left", fill="y", pady=10, padx=10)

        # create label "quản lý học sinh"
        ctk.CTkLabel(self.form_frame, text="Quản lý học sinh", font=("Arial", 30)).pack(padx=10, pady=20)

        # crate form input tên hoc sinh
        # label + Entry
        ctk.CTkLabel(self.form_frame, text="Ten hoc sinh: ").pack(anchor="w", padx=10)
        self.name_entry = ctk.CTkEntry(self.form_frame, width=250)
        self.name_entry.pack(pady=5)

        # create form tuổi học sinh
        ctk.CTkLabel(self.form_frame, text="Tuổi học sinh: ").pack(anchor="w", padx=10)
        self.age_entry = ctk.CTkEntry(self.form_frame, width=250)
        self.age_entry.pack(pady=5)

        # create form lớp hoc
        ctk.CTkLabel(self.form_frame, text="Lớp học: ").pack(anchor="w", padx=10)
        self.class_entry = ctk.CTkEntry(self.form_frame, width=250)
        self.class_entry.pack(pady=5)

        # tạo button thêm, xóa và sửa
        self.add_button = ctk.CTkButton(self.form_frame, text="Thêm học sinh", command=self.add_student)
        self.add_button.pack(pady=10)

        self.edit_button = ctk.CTkButton(self.form_frame, text="Sửa thông tin học sinh")
        self.edit_button.pack(pady=10)

        self.remove_button = ctk.CTkButton(self.form_frame, text="Xóa học sinh")
        self.remove_button.pack(pady=10)

        # tạo display information student
        self.display_frame = ctk.CTkFrame(self, corner_radius=10)

        self.display_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # create label "Danh sách học sinh"
        ctk.CTkLabel(self.display_frame, text="Danh sách học sinh", font=("Arial", 30)).pack(padx=10, pady=20)

        # create textbox
        self.student_listbox = ctk.CTkTextbox(self.display_frame, font=("Arial", 20), wrap="none")
        self.student_listbox.configure(state="disabled")
        self.student_listbox.pack(pady=10, padx=10, fill="both", expand=True)

if __name__ == "__main__":
    app = StudentManager()

    # start app
    app.mainloop()