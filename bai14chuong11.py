def xu_ly_set(A, B):
    
    hieu_a_b = []
    for phan_tu in A:
        co_trong_b = False
        for pt_b in B:
            if phan_tu == pt_b:
                co_trong_b = True
                break 
        if not co_trong_b:
            hieu_a_b.append(phan_tu)

    hieu_b_a = []
    for phan_tu in B:
        co_trong_a = False
        for pt_a in A:
            if phan_tu == pt_a:
                co_trong_a = True
                break
        if not co_trong_a:
            hieu_b_a.append(phan_tu)
            
    giao_a_b = []
    for phan_tu in A:
        for pt_b in B:
            if phan_tu == pt_b:
                giao_a_b.append(phan_tu)
                break
                
    return hieu_a_b, hieu_b_a, giao_a_b

set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}
hieu1, hieu2, giao = xu_ly_set(list(set_A), list(set_B)) 
print(f"Set A: {set_A}")
print(f"Set B: {set_B}")
print(f"Phần tử thuộc A nhưng không thuộc B: {hieu1}") 
print(f"Phần tử thuộc B nhưng không thuộc A: {hieu2}") 
print(f"Phần tử có trong cả hai set (Giao): {giao}") 