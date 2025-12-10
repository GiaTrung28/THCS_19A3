def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

so_n = 17 

if kiem_tra_so_nguyen_to(so_n):
    print(f"Số {so_n} LÀ số nguyên tố.")
else:
    print(f"Số {so_n} KHÔNG phải là số nguyên tố.")

print("\nCác số nguyên tố trong khoảng [100, 500] là:")
for so in range(100, 501):
    if kiem_tra_so_nguyen_to(so):
        print(so, end=" ")

print() 