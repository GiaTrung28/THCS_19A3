import math

def la_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def in_so_nguyen_to_trong_khoang(a, b):
    print(f"Các số nguyên tố trong khoảng từ {a} đến {b} là:")
    for num in range(a, b + 1):
        if la_so_nguyen_to(num):
            print(num, end=" ")
    print() 

print(f"Số 29 có phải là số nguyên tố không? {la_so_nguyen_to(29)}")
print(f"Số 4 có phải là số nguyên tố không? {la_so_nguyen_to(4)}")
in_so_nguyen_to_trong_khoang(10, 50)
