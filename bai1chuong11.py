s = input("Nhập chuỗi: ")
chu_cai = 0
chu_so = 0
ky_tu_dac_biet = 0
for char in s:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        chu_cai += 1
    elif '0' <= char <= '9':
        chu_so +=1
    else:
        ky_tu_dac_biet += 1
        print(f"Số lượng chữ cái: {chu_cai}")
        print(f"Số lượng chữ số: {chu_so}")
        print(f"Số lượng ký tự đặc biết: {ky_tu_dac_biet}")
