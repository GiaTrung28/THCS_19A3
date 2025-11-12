# Bài 5: Nhập số tiền gửi ban đầu và lãi suất hàng năm từ bàn phím. Tính số tiền lãi nhận được sau 1 tháng, 2 quý, 3 năm (lãi đơn).

# Giả định dữ liệu nhập vào (ví dụ)
so_tien_ban_dau = 10000000 # 10 triệu VND
lai_suat_nam = 0.06 # 6% mỗi năm

# Tính toán lãi đơn cho các kỳ hạn
lai_1_thang = so_tien_ban_dau * lai_suat_nam * (1/12)
lai_2_quy = so_tien_ban_dau * lai_suat_nam * (2/4)
lai_3_nam = so_tien_ban_dau * lai_suat_nam * 3

# In kết quả
print(f"Tiền lãi sau 1 tháng: *{round(lai_1_thang, 2)}* VND")
print(f"Tiền lãi sau 2 quý: *{round(lai_2_quy, 2)}* VND")
print(f"Tiền lãi sau 3 năm: *{round(lai_3_nam, 2)}* VND")
