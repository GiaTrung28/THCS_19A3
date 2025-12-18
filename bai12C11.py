def nhan_hai_ma_tran(ma_tran_A, ma_tran_B):
    hang_A = len(ma_tran_A)
    cot_A = len(ma_tran_A[0])
    hang_B = len(ma_tran_B)
    cot_B = len(ma_tran_B[0])

    if cot_A != hang_B:
        return None, "Không thể nhân hai ma trận vì số cột của A không bằng số hàng của B."

    ma_tran_C = []
    for i in range(hang_A):
        hang_moi = []
        for j in range(cot_B):
            hang_moi.append(0)
        ma_tran_C.append(hang_moi)

    for i in range(hang_A): 
        for j in range(cot_B): 
            tong_tich = 0
            for k in range(cot_A): 
                tong_tich += ma_tran_A[i][k] * ma_tran_B[k][j]
            ma_tran_C[i][j] = tong_tich
            
    return ma_tran_C, "Phép nhân thành công."

matrix_A_input = [
    [1, 2, 3],
    [4, 5, 6]
]
matrix_B_input = [
    [7, 8],
    [9, 1],
    [2, 3]
]
result_matrix, msg = nhan_hai_ma_tran(matrix_A_input, matrix_B_input)
print(f"Ma trận A: {matrix_A_input}")
print(f"Ma trận B: {matrix_B_input}")
print(f"Kết quả nhân hai ma trận: {result_matrix}")
print(f"Trạng thái: {msg}")