def tinh_tong_chu_so(n):
    if n == 0:
        return 0
    else:
        return (n % 10 + tinh_tong_chu_so(int(n / 10)))

so_can_tinh = 12345
tong = tinh_tong_chu_so(so_can_tinh)
print(f"Tổng các chữ số của số {so_can_tinh} là: {tong}")
