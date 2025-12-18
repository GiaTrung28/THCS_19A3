chuoi_nhap = input("Nhập một chuỗi: ")
n_str = input("Nhập độ dài n: ")
n = int(n_str)
tu_hien_tai = ""
danh_sach_tu = []

for ky_tu in chuoi_nhap:
    if ky_tu == ' ':
        if tu_hien_tai:
            danh_sach_tu.append(tu_hien_tai)
            tu_hien_tai = ""
    else:
        tu_hien_tai += ky_tu
if tu_hien_tai:
    danh_sach_tu.append(tu_hien_tai)

tu_dai_hon_n = []
for tu in danh_sach_tu:
    do_dai = 0
    for _ in tu:
        do_dai += 1
    if do_dai > n:
        tu_dai_hon_n.append(tu)

print(f"Các từ có độ dài lớn hơn {n}: {tu_dai_hon_n}")
