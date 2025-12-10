def tim_so_le_lon_nhat(a, b, c):
    so_le_tim_duoc = []
    for num in [a, b, c]:
        if num % 2 != 0:
            so_le_tim_duoc.append(num)
    
    if not so_le_tim_duoc:
        return -1
    else:
        return max(so_le_tim_duoc)

print(f"Số lẻ lớn nhất trong (1, 2, 3) là: {tim_so_le_lon_nhat(1, 2, 3)}")
print(f"Số lẻ lớn nhất trong (2, 4, 6) là: {tim_so_le_lon_nhat(2, 4, 6)}")
print(f"Số lẻ lớn nhất trong (5, 1, 9) là: {tim_so_le_lon_nhat(5, 1, 9)}")
