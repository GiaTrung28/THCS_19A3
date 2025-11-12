# Bài 1: Nhập giá sản phẩm và số lượng mua từ bàn phím. Tính tổng chi phí và thuế VAT (10%).
# In tổng tiền phải trả, làm tròn đến 2 chữ số thập phân.

# Giả định dữ liệu nhập vào (ví dụ)
gia_san_pham = 50.0
so_luong = 3

# Tính toán
tong_chi_phi = gia_san_pham * so_luong
thue_vat = tong_chi_phi * 0.10
tong_tien_phai_tra = tong_chi_phi + thue_vat

# In kết quả đã làm tròn
print(f"Tổng tiền phải trả (làm tròn): *{round(tong_tien_phai_tra, 2)}* VND")