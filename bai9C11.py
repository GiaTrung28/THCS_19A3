def tinh_tong_cheo_phu(ma_tran):
    n = len(ma_tran) 
    tong = 0
    for i in range(n):
        j = n - 1 - i
        tong += ma_tran[i][j]
    return tong

matrix_input = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
total = tinh_tong_cheo_phu(matrix_input)
print(f"Ma trận đầu vào: {matrix_input}")
print(f"Tổng các phần tử trên đường chéo phụ là: {total}") 
