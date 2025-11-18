def tim_uoc_chung_lon_nhat():
    """Nhập hai số và tìm ƯCLN của chúng bằng thuật toán Euclidean."""
    try:
        a = int(input("Nhập số thứ nhất (a): "))
        b = int(input("Nhập số thứ hai (b): "))
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng nhập số nguyên.")
        return

    a = abs(a)
    b = abs(b)

    while b:
        a, b = b, a % b
    
    print(f"Ước chung lớn nhất của {abs(int(input('Nhập số thứ nhất (a): ')))} và {abs(int(input('Nhập số thứ hai (b): ')))} là: {a}")

