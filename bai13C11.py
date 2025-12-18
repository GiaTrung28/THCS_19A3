def kiem_tra_ma_tran_don_vi(ma_tran):
    n = len(ma_tran)
    for hang in ma_tran:
        if len(hang) != n:
            return False, "Ma trận không phải là ma trận vuông."

    for i in range(n):
        for j in range(n):
            if i == j:
                if ma_tran[i][j] != 1:
                    return False, "Phần tử trên đường chéo chính không bằng 1."
            else:
                if ma_tran[i][j] != 0:
                    return False, "Phần tử ngoài đường chéo chính không bằng 0."
                    
    return True, "Ma trận là ma trận đơn vị."

identity_matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
is_identity, msg = kiem_tra_ma_tran_don_vi(identity_matrix)
print(f"Ma trận đầu vào: {identity_matrix}")
print(f"Kết quả kiểm tra: {msg}")

non_identity_matrix = [
    [1, 0, 0],
    [0, 2, 0],
    [0, 0, 1]
]
is_identity, msg = kiem_tra_ma_tran_don_vi(non_identity_matrix)
print(f"Ma trận đầu vào: {non_identity_matrix}")
print(f"Kết quả kiểm tra: {msg}")