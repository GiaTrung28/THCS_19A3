danh_sach_goc = [12, 24, 10, 24, 12, 92, 5, 92]
danh_sach_moi = []

for phan_tu in danh_sach_goc:
    co_trong_danh_sach_moi = False
    for phan_tu_moi in danh_sach_moi:
        if phan_tu == phan_tu_moi:
            co_trong_danh_sach_moi = True
            break
    if not co_trong_danh_sach_moi:
        danh_sach_moi.append(phan_tu)

print(f"Danh sách sau khi loại bỏ trùng lặp: {danh_sach_moi}")
