def la_so_hoan_hao(n):
    if n <= 1:
        return False
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n

def tinh_tong_so_hoan_hao(a, b):
    tong_cac_so_hoan_hao = 0
    for num in range(a, b + 1):
        if la_so_hoan_hao(num):
            tong_cac_so_hoan_hao += num
    return tong_cac_so_hoan_hao

tong = tinh_tong_so_hoan_hao(1, 1000)
print(f"Tổng của tất cả các số hoàn hảo trong khoảng từ 1 đến 1000 là: {tong}")