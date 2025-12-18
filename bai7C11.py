danh_sach_so = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tong_muc_tieu = 10
cap_so = []

for i in range(len(danh_sach_so)):
    for j in range(i + 1, len(danh_sach_so)):
        if danh_sach_so[i] + danh_sach_so[j] == tong_muc_tieu:
            cap_so.append((danh_sach_so[i], danh_sach_so[j]))

print(f"Các cặp số có tổng bằng {tong_muc_tieu}: {cap_so}")
