gia_san_pham = float(input("Nhập giá sản phẩm: "))
so_luong_mua = int(input("Nhập số lượng mua: "))

tong_chi_phi = gia_san_pham * so_luong_mua

thue_vat = tong_chi_phi * 0.10

tong_tien_phai_tra = tong_chi_phi + thue_vat

print(f"Tổng tiền phải trả: {tong_tien_phai_tra:.2f} VNĐ")