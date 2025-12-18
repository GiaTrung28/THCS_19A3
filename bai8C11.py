danh_sach_goc = [1, 2, 3, 4, 5]
k = 2 

k = k % len(danh_sach_goc)

danh_sach_moi = []
for i in range(len(danh_sach_goc) - k, len(danh_sach_goc)):
    danh_sach_moi.append(danh_sach_goc[i])
for i in range(len(danh_sach_goc) - k):
    danh_sach_moi.append(danh_sach_goc[i])

print(f"Danh sách sau khi dịch chuyển {k} vị trí sang phải: {danh_sach_moi}")