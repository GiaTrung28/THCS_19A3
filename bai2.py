
tong_so_keo = int(input("Nhập tổng số kẹo: "))
so_hoc_sinh = int(input("Nhập số học sinh: "))

keo_moi_hs = tong_so_keo // so_hoc_sinh

keo_con_thua = tong_so_keo % so_hoc_sinh

print(f"Số kẹo mỗi học sinh nhận được: {keo_moi_hs} cái")
print(f"Số kẹo còn thừa: {keo_con_thua} cái")
