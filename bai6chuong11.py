danh_sach_so = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tong_chan = 0
tong_le = 0

for so in danh_sach_so:
    if so % 2 == 0:
        tong_chan += so
    else:
        tong_le += so

print(f"Tổng các số chẵn: {tong_chan}")
print(f"Tổng các số lẻ: {tong_le}")