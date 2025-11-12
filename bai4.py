# Bài 4: Nhập một số tiền bằng VNĐ từ bàn phím. Chuyển đổi số tiền đó sang USD (tỷ giá 1 USD = 24.500 VNĐ) và in kết quả, làm tròn đến 2 chữ số thập phân.

# Giả định dữ liệu nhập vào (ví dụ)
so_tien_vnd = 5000000 # 5 triệu VND
ty_gia = 24500

# Tính toán
so_tien_usd = so_tien_vnd / ty_gia

# In kết quả đã làm tròn
print(f"Số tiền USD nhận được: *{round(so_tien_usd, 2)}* USD")
