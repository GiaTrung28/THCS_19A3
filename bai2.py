# Bài 2: Nhập tổng số kẹo và số học sinh từ bàn phím. Tính số kẹo mỗi học sinh nhận được và số kẹo còn thừa (biết số kẹo mỗi học sinh nhận đều như nhau).

# Giả định dữ liệu nhập vào (ví dụ)
tong_so_keo = 100
so_hoc_sinh = 17

# Tính toán
keo_moi_hoc_sinh = tong_so_keo // so_hoc_sinh # Phép chia lấy phần nguyên
keo_con_thua = tong_so_keo % so_hoc_sinh # Phép chia lấy phần dư

# In kết quả
print(f"Số kẹo mỗi học sinh nhận được: *{keo_moi_hoc_sinh}*")
print(f"Số kẹo còn thừa: *{keo_con_thua}*")