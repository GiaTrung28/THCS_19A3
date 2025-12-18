def kiem_tra_doi_xung(ma_tran):
    n = len(ma_tran)
    for hang in ma_tran:
        if len(hang) != n:
            return False, "Ma trận không phải là ma trận vuông"
            
    for i in range(n):
        for j in range(i + 1, n): 
            if ma_tran[i][j] != ma_tran[j][i]:
                return False, "Ma trận không đối xứng"
                
    return True, "Ma trận là ma trận đối xứng"

sym_matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]
is_sym, msg = kiem_tra_doi_xung(sym_matrix)
print(f"Ma trận đầu vào: {sym_matrix}")
print(f"Kết quả kiểm tra: {msg}")

non_sym_matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 9] 
]
is_sym, msg = kiem_tra_doi_xung(non_sym_matrix)
print(f"Ma trận đầu vào: {non_sym_matrix}")
print(f"Kết quả kiểm tra: {msg}")