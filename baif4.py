def tinh_trung_binh_cong(a, b, c):
    trung_binh = (a + b + c) / 3
    return trung_binh

so1, so2, so3 = 10, 20, 30
gia_tri_trung_binh = tinh_trung_binh_cong(so1, so2, so3)
print(f"Giá trị trung bình cộng của {so1}, {so2}, {so3} là: {gia_tri_trung_binh}")
