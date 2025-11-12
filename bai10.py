# Bài 10: Nhập mức lương cơ bản và số ngày công trong tháng từ bàn phím.
# Lương một ngày được tính bằng lương_cơ_bản / 22.
# Tiền thưởng là 10% nếu số ngày công trên 22 ngày.
# Tiền phạt là 5% nếu số ngày công dưới 22 ngày.
# Tính và in ra tổng tiền lương thực nhận của nhân viên (chỉ sử dụng kiến thức đã học).

# Giả định dữ liệu nhập vào (ví dụ 1: đủ công)
luong_co_ban_1 = 10000000
so_ngay_cong_1 = 22

# Giả định dữ liệu nhập vào (ví dụ 2: có thưởng)
luong_co_ban_2 = 10000000
so_ngay_cong_2 = 25

# Giả định dữ liệu nhập vào (ví dụ 3: bị phạt)
luong_co_ban_3 = 10000000
so_ngay_cong_3 = 20

def tinh_luong_thuc_nhan(luong_co_ban, so_ngay_cong):
    """Hàm trợ giúp tính lương thực nhận"""
    luong_mot_ngay = luong_co_ban / 22
    tong_luong_chua_thuong_phat = luong_mot_ngay * so_ngay_cong
    ty_le_phu_cap = 0

    if so_ngay_cong > 22:
        ty_le_phu_cap = 0.10 # Thưởng 10%
    elif so_ngay_cong < 22:
        ty_le_phu_cap = -0.05 # Phạt 5%

    tien_thuong_phat = tong_luong_chua_thuong_phat * ty_le_phu_cap
    luong_thuc_nhan = tong_luong_chua_thuong_phat + tien_thuong_phat
    return luong_thuc_nhan

# Tính và in kết quả
print(f"Lương thực nhận (Ví dụ 1 - đủ công): *{round(tinh_luong_thuc_nhan(luong_co_ban_1, so_ngay_cong_1), 2)}* VND")
print(f"Lương thực nhận (Ví dụ 2 - có thưởng): *{round(tinh_luong_thuc_nhan(luong_co_ban_2, so_ngay_cong_2), 2)}* VND")
print(f"Lương thực nhận (Ví dụ 3 - bị phạt): *{round(tinh_luong_thuc_nhan(luong_co_ban_3, so_ngay_cong_3), 2)}* VND")
