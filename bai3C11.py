chuoi_nhap = input("Nhập một chuỗi có nhiều khoảng trắng: ")
chuoi_moi = ""
khoang_trang_truoc = False

for ky_tu in chuoi_nhap:
    if ky_tu == ' ':
        if not khoang_trang_truoc:
            chuoi_moi += ' '
            khoang_trang_truoc = True
    else:
        chuoi_moi += ky_tu
        khoang_trang_truoc = False

chuoi_da_xu_ly = ""
bat_dau = 0
ket_thuc = 0
for i in range(len(chuoi_moi)):
    if chuoi_moi[i] != ' ':
        bat_dau = i
        break
for i in range(len(chuoi_moi) - 1, -1, -1):
    if chuoi_moi[i] != ' ':
        ket_thuc = i
        break
for i in range(bat_dau, ket_thuc + 1):
    chuoi_da_xu_ly += chuoi_moi[i]

print(f"Chuỗi sau khi xử lý: '{chuoi_da_xu_ly}'")
