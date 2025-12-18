def tim_hang_tong_lon_nhat(ma_tran):
    max_tong = None
    chi_so_hang_max = -1

    for i in range(len(ma_tran)):
        hang_hien_tai = ma_tran[i]
        tong_hang = 0
        for phan_tu in hang_hien_tai:
            tong_hang += phan_tu

        if max_tong is None or tong_hang > max_tong:
            max_tong = tong_hang
            chi_so_hang_max = i
            
    return chi_so_hang_max, max_tong

matrix_input_10 = [
    [10, 2, 3], 
    [1, 50, 6], 
    [7, 8, 9]  
]
index, max_val = tim_hang_tong_lon_nhat(matrix_input_10)
print(f"Ma trận đầu vào: {matrix_input_10}")
print(f"Hàng có tổng lớn nhất là hàng thứ {index} (chỉ số 0), với tổng là {max_val}")