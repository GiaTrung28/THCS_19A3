danh_sach_so = [10, 20, 4, 45, 99, 1, 45, 99]

lon_nhat = danh_sach_so[0]
lon_thu_hai = danh_sach_so[0]

for so in danh_sach_so:
    if so > lon_nhat:
        lon_nhat = so

for so in danh_sach_so:
    if so > lon_thu_hai and so < lon_nhat:
        lon_thu_hai = so
        
if lon_thu_hai == lon_nhat:
    print("Không tìm thấy giá trị lớn thứ hai (tất cả các số đều giống nhau hoặc chỉ có một giá trị duy nhất sau khi loại bỏ trùng lặp).")
else:
    print(f"Giá trị lớn thứ hai là: {lon_thu_hai}")