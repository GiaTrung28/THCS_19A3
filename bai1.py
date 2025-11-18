import math
def kiem_tra_so_chinh_phuong():
    
    """Nhập một số và kiểm tra xem nó có phải là số chính phương hay không."""
    try:
        n = int(input("Nhập một số nguyên dương: "))
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng nhập số nguyên.")
        return

    if n < 0:
        print(f"{n} không phải là số chính phương (số âm).")
        return

    can_bac_hai_nguyen = int(math.isqrt(n))

    if can_bac_hai_nguyen * can_bac_hai_nguyen == n:
        print(f"{n} là số chính phương vì {can_bac_hai_nguyen}^2 = {n}.")
    else:
        print(f"{n} không phải là số chính phương.")

