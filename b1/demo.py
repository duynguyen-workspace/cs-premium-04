
# TODO: CÚ PHÁP PYTHON

''' 
#? Quy tắc đặt tên biến:
1. Đặt tiếng việt hết hoặc tiếng anh
2. Đặt tên theo kiểu snake_case
3. Tên biến không được bắt đầu bằng số
''' 

ho_ten = "Nguyen Van A"

#? Lệnh xuất
print(2)

''' 
#? Cách để tạo ghi chú nhanh:
1. Tổ hợp: Ctrl (Cmd) + /
2. Đặt tên theo kiểu snake_case
''' 

# print("Abc")
# print(ho_ten)

''' 
#? Kiểu dữ liệu: 
1. str (string): chuỗi - bao gồm tất cả các kí tự được quy định trong bảng ASCII / Unicode
2. int (integer): số nguyên 
3. float: số thực / số hữu tỉ 
4. bool (boolean): giá trị dùng để so sánh (True, False) = (1, 0)
Lưu ý: dùng type() để in ra kiểu dữ liệu của giá trị đó
'''
print(5 > 3)

print("Kiểu số nguyên(int):", type(5))
print("Kiểu số thực(float):", type(5.0))

#? Lệnh nhập => luôn trả về kiểu dữ liệu string
tuoi = int(input("Nhập vào tuổi của bạn: ")) # "20" -> 20
print("Bạn có trên 18 tuổi không:", tuoi > 18)

'''
#? Toán tử
1. Các phép toán tử số học: +, -, *, / (cộng, trừ, nhân, chia)
2. Các phép toán tử so sánh: ==, !=, >=, <= (bằng nhau, không bằng, lớn hơn, bé hơn)
3. Các toán tử khác: %, +=, -=, *=, /=
'''
a = 10
b = 5

print(a + b)
print(a / b) # Lưu ý: phép chia sẽ ép kiểu số từ int sang float (vd: 10 / 2 == 5.0 chứ != 5)

print("5" * 3) # Kết quả: "555", python sẽ tạo 1 chuỗi có gía trị được lặp lại bằng số lần nhân lên

print("5" + 3) # Lưu ý: phép tính này sẽ bị lỗi vì python k cho phép cộng chuỗi với số

'''
#? Các loại hàm (function):
1. Hàm không trả về giá trị (void)
2. Hàm trả về giá trị
'''

# Hàm không trả về giá trị
def in_ho_ten():
    ho_ten = "Duy"
    print(ho_ten)

# Hàm nhận vào tham số (argument / parameter) và trả về giá trị:
def kiem_tra_tuoi(num): # num là giá trị truyền vào
    is_older_than_18 = False
    
    if num > 18:
        is_older_than_18 = True
    else:
        is_older_than_18 = False
        
    return is_older_than_18


'''
#? Scope: phạm vi của biến
1. Local (Function) scope: những biến chỉ tồn tại trong phạm vi hàm, vòng lặp
2. Global scope: biến toàn cục, được sử dụng cho tất cả mọi nơi
'''

x = 10 # Nếu không có dòng này thì dòng change_x() sẽ lỗi

def change_x():
    x = 20 

change_x()
print("x:", x)

'''
#? Vòng lặp:
1. Vòng lặp for: sử dụng khi cần lặp qua các giá trị trong 1 khoảng nhất định
2. Vòng lặp while: sử dụng khi cần lặp với điều kiện nhất định

#! Quy tắc khi sử dụng vòng lặp:
Phải luôn có 1 biến (tạm) để lưu giá trị cần dừng vòng lặp
'''

#* range(a, b): a sẽ là giá trị bắt đầu, b - 1 là giá trị kết thúc
#* range(a, b, c): a với b giống ở trên, c là step (khoảng cách giữa các giá trị giữa vòng lặp) 
for i in range(1, 11, 2):
    print(i)
    
'''
Điều kiện while: 
1. trả về kiểu dữ liệu boolean
2. phải có dòng lệnh để thay đổi gía trị qui định kết thúc vòng lặp
'''
i = 0
while i < 10:
    print(i)
    i += 1

#TODO: CTDL PYTHON: set, tuples, list, dictionary

''' 
#? Set: 
1. Khai báo: {} hoặc set()
2. Không được sắp xếp -> mình không thể lấy giá trị của phần tử theo index
3. Không chứa dữ liệu trùng lặp -> bỏ hết dữ liệu trùng lặp nếu khai báo
4. Không thay đổi (tương tác) được với phần tử trong set
'''

# C1: my_set = set([1, 2, 3, 4, 5])
my_set = {1, 2, 2, 3, 4, 5, 5, 5, 6, "1"}
print(my_set)
print("Chiều dài set:", len(my_set))

''' 
#? Tuples: 
1. Khai báo: ()
2. Không được sắp xếp (mình vẫn lấy giá trị của phần tử theo index)
3. Không thay đổi (tương tác) được với phần tử trong tuples
4. Chứa được dữ liệu trùng lặp

VD: toạ độ của 1 vị trí (x, y), danh sách giá sản phẩm ($4, $5, ...)
'''
my_tuples = (100, 200, 300, 400, 100, 200)
print(my_tuples)

print("Chiều dài của tuples:", my_tuples)

'''
#? List (mảng, giống array):
1. Khai báo: [] hoặc list()
2. Có thể được sắp xếp -> lấy giá trị của phần tử theo index
3. Tương tác được với phần tử trong list: thêm, xoá, sửa = CRUD
4. Chứa được dữ liệu trùng lặp
'''
my_list = [2, 5, 6, 4, 9] 

# Thêm phần tử vào mảng
my_list.append(6)
print("List được thêm vào: ", my_list) # [2, 5, 6, 4, 9, 6]

# Xoá phần tử khỏi mảng
my_list.pop() # Xoá giá trị cuối cùng (k có tham số), nếu có tham số -> xoá theo index
my_list.remove(2) # Remove: xoá hết toàn bộ giá trị được truyền vào hàm

print("List được xoá: ", my_list)

my_list.sort() # Sắp xếp các giá trị tăng dần (mặc định) -> [2, 4, 5, 6, 6, 9]
print("List được sắp xếp:", my_list)

print("Chiều dài list:", len(my_list))

# Vòng lặp các phần tử trong mảng
for item in my_list:
    print(item)


'''
#? Filter giá trị cho mảng
C1: dùng cú pháp for in như bình thường
C2: dùng cú pháp list comprehension
'''
# C1 -> cách dài nhưng đơn giản
result_list = []
for item in my_list:
    if (item % 2 == 0): # MOD
        result_list.append(item)
        
print(result_list)
        
# C2 -> cách ngắn gọn hơn nhiều        
result_list = [item for item in my_list if item % 2 == 0]
print(result_list)

'''
#? Dictionary (từ điển, giống với object / JSON) :
1. Khai báo: {}, chứa các phần tử là 1 cặp key (bắt buộc là chuỗi) - value (kiểu dữ liệu nào cũng được)
2. Lấy gía trị (my_dict.values()), lấy key (my_dict.keys()), lấy cả 2 (my_dict.items())
3. Tương tác được với phần tử trong list: thêm, xoá, sửa = CRUD
4. Không được chứa key trùng lặp, giá trị của từng key thì không ảnh hướng
5. Không sắp xếp được
'''
my_dict = {
    "name": "Nguyen Duy", 
    "age": 18,
    "phone": 123456
}

#? Vòng lặp lấy dữ liệu trong dictionary:

# Vòng lặp lấy cả key và value
for key, value in my_dict.items():
    print(key, value)

# Thêm key và value    
my_dict["job"] = "Giang Vien"
print("Dictionary được thêm: ", my_dict)

# Cập nhật key và value
my_dict["age"] = 20
print("Dictionary được cập nhật: ", my_dict)

# Xoá key và value
my_dict.popitem() # Xoá cặp key - value ở cuối của dict
print("Dictionary bị xoá: ", my_dict)

my_dict.pop("age") # Xoá cặp key - value có giá trị là key được truyền vào
print("Dictionary bị xoá tuổi: ", my_dict)


'''
#? Các kiểu dữ liệu (nâng cao)
1. immutable - bất biến: str, int, float, boolean, tuple -> nó sẽ luôn tạo ra đối tượng mới khi gán lại giá trị của 1 biến cho biến khác
2. mutable - có biến: giá trị của biến này khi gán cho biến khác -> địa chỉ cấp phát bộ nhớ, không lưu giá trị
'''

#! Demo kiểu dữ liệu immutable
a = 10
b = a # biến b được cấp phát bộ nhớ mới với giá trị b = 10 

a += 50 # biến a được cập nhật giá trị -> a = 60

print("a:",a) # 60
print("b:",b) # 10

#! Demo kiểu dữ liệu mutable
a = [1, 2, 3, 4, 5] 
b = a # không lưu [1, 2, 3, 4, 5] -> lưu địa chỉ của a (VD: aaaa1234 - địa chỉ bộ nhớ của biến a)

b.append(6) # lúc này b và a có cùng địa chỉ -> vẫn cập nhật mảng cũ [1, 2, 3, 4, 5, 6]
a.append(7) # -> vẫn cập nhật mảng cũ [1, 2, 3, 4, 5, 6, 7]

print("a:", a) 
print("b:", b)
# -> a và b đều có giá trị giống nhau


'''
#? Khác: chủ để i++ và ++i trong ngôn ngữ khác
i++, ++i đều tăng i lên 1. Tuy nhiên:
. ++i -> tăng i trước rồi mới thực thi lệnh
. i++ -> thực thi lệnh trước rồi mới tăng i

VD:
a = 5
b = a++ # giá trị của b vẫn = 5, vì gán b = 5 trước khi tăng a
print("b lần 1": b) # b = 5
b = ++a # giá trị của b = 7, vì lúc này a bằng 6 -> được tăng 1 đơn vị là 7, trước khi gán cho b
print("b lần 2": b) # b = 7
'''