#TODO: Tạo class trong Python -> mutable 
# Lưu ý: 
# - tên class sẽ viết liền vào nhau, chữ cái đầu luôn viết hoa
# - bắt buộc phải có phương thức khởi tạo

# Class - Lớp
class SinhVien: 
    # Phương thức khởi tạo
    def __init__(self, maSV, tenSV, toan, van, hoa):
        self.maSV = maSV
        self.tenSV = tenSV
        self.toan = toan
        self.van = van
        self.hoa = hoa
    
    # Phương thức tính điểm trung bình
    def tinh_diem_trung_binh(self):
        return (self.toan + self.van + self.hoa) / 3 # int -> float

class NhanVien:
    # Phương thức khởi tạo
    def __init__(self, maNV, tenNV, luong, danhGia):
        self.maNV = maNV
        self.tenNV = tenNV
        self.luong = luong
        self.danhGia = danhGia
        
    # Phương thức tính lương
    def tinh_luong(self):
        if (self.danhGia > 8):
            return self.luong * 2
        elif (self.danhGia > 5):
            return self.luong
        else:
            return self.luong * 0.5

# Sinh Viên
sinhVienA = SinhVien(1, "Nguyen Van A", 10, 9, 8)
sinhVienB = SinhVien(2, "Nguyen Van B", 8, 9, 7)
sinhVienC = SinhVien(3, "Nguyen Van C", 7, 8, 9)

print("Mã SV:", sinhVienA.maSV)
print("Điểm Toán SV:", sinhVienA.toan)

print("Điểm TB SV:", sinhVienA.tinh_diem_trung_binh())
    
# Nhân Viên
nhanVienA = NhanVien(1, "Tran Thi B", 500, 10)

print("Lương NV: $" + str(nhanVienA.tinh_luong()))

# QuanLy va GiamDoc -> tính chất đầu tiên OOP: kế thừa