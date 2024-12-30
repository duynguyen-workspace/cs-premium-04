# Tạo danh sách sinh viên
danh_sach_SV = [
    {
        "maSV": 1, 
        "hoVaTen": "Nguyen Van A",
        "toan": 10,
        "van": 6,
        "hoa": 8, # TB: 8.0
        "ly": 10
    },
    {
        "maSV": 2,
        "hoTen": "Tran Thi B",
        "toan": 5.5,
        "van": 8,
        "hoa": 4 # 17.5 / 3 -> lớn hơn 5
    },
    {
        "maSV": 3,
        "tenSV": "Luong Gia C",
        "toan": 9,
        "van": 9,
        "hoa": 9 # 9 -> lớn hơn 5
    },
    {
        "maSV": 4,
        "tenSV": "Mai Van D",
        "diemToan": 4,
        "diemVan": 4,
        "diemHoa": 5 # -> nhỏ hơn 5
    },
    {
        "maSV": 5,
        "tenSV": "Nguyen Thi E",
        "toan": 1,
        "van": 2,
        "hoa": 3 # -> nhỏ hơn 5
    },
]

# Hàm in ra thông tin Sinh Viên có điểm trung bình lớn hơn 5
def tinh_diem_trung_binh(toan, van, hoa):
    return (toan + van + hoa) / 3 # int -> float

def in_thong_tin_sv_lon_hon_5():
    for sv in danh_sach_SV:
        diemToan = sv["toan"]
        diemVan = sv["van"]
        diemHoa = sv["hoa"]
        
        diemTB = tinh_diem_trung_binh(diemToan, diemVan, diemHoa)
        
        if (diemTB > 5.0):
            print(f"""
----------
Mã SV: {sv["maSV"]}
Họ Tên: {sv["tenSV"]}
Điểm Trung Bình: {diemTB}
----------
""")
        

in_thong_tin_sv_lon_hon_5()