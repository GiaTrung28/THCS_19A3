def kiem_tra_nguyen_to(num):
    """Kiểm tra xem một số có phải là số nguyên tố hay không."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def tim_cac_so_nguyen_to_nho_hon_n():
    """Nhập n và in ra tất cả các số nguyên tố nhỏ hơn n."""
    try:
        n = int(input("Nhập số nguyên n: "))
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng nhập số nguyên.")
        return

    if n <= 2:
        print(f"Không có số nguyên tố nào nhỏ hơn {n}.")
        return

    danh_sach_so_nguyen_to = []
    for i in range(2, n):
        if kiem_tra_nguyen_to(i):
            danh_sach_so_nguyen_to.append(i)
    
    print(f"Các số nguyên tố nhỏ hơn {n} là: {danh_sach_so_nguyen_to}")

