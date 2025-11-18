import math

n_str = input("Nhập một số nguyên dương n: ")
if not n_str.isdigit():
    print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên dương.")
else:
    n = int(n_str)
    if n < 0:
        print("Vui lòng nhập một số nguyên dương.")
    else:
        sqrt_n = math.sqrt(n)
        if sqrt_n.is_integer():
            print(f"{n} là số chính phương.")
        else:
            print(f"{n} không phải là số chính phương.")