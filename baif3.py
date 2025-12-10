def kiem_tra_so_armstrong(n):
    so_chu_so = len(str(n))
    tong_luy_thua = 0
    temp = n

    while temp > 0:
        chu_so = temp % 10
        tong_luy_thua += chu_so ** so_chu_so
        temp //= 10 

    return tong_luy_thua == n

print(f"Số 153 có phải số Armstrong không? {kiem_tra_so_armstrong(153)}")
print(f"Số 123 có phải số Armstrong không? {kiem_tra_so_armstrong(123)}")
