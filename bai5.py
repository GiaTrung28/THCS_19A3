def tinh_cac_phep_tinh(n):
    """Tính toán các biểu thức S1, S2, S3, S4 với đầu vào là n."""
    try:
        n = int(n)
    except ValueError:
        print("Đầu vào n không hợp lệ. Vui lòng nhập số nguyên.")
        return

    S1 = n * (n + 1) // 2

    S2 = 1
    if n > 1:
        for i in range(1, n):
            S2 *= i
    elif n <= 1: 
        S2 = 1
        
    S3 = 0.0
    for k in range(1, n + 1):
        S3 += ((-1)**k) / k
        
    S4 = 0.0
    for k in range(n + 1):
        if k + 2 != 0: 
            S4 += k / (k + 2)

    print(f"Kết quả với n = {n}:")
    print(f"S1 = {S1}")
    print(f"S2 = {S2}")
    print(f"S3 = {S3:.6f} (Lưu ý về dấu theo công thức đề bài)")
    print(f"S4 = {S4:.6f}")
