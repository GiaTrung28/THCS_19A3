import math

def gcd(a, b):
    """Hàm tìm ƯCLN (sử dụng cho việc tối giản)"""
    while b:
        a, b = b, a % b
    return a

def toi_gian_phan_so():
    """Nhập tử số và mẫu số, sau đó trả về phân số tối giản."""
    try:
        tu_so = int(input("Nhập tử số: "))
        mau_so = int(input("Nhập mẫu số: "))
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng nhập số nguyên.")
        return

    if mau_so == 0:
        print("Lỗi: Mẫu số không được bằng 0.")
        return

    ucln = gcd(abs(tu_so), abs(mau_so))
    
    tu_toi_gian = tu_so // ucln
    mau_toi_gian = mau_so // ucln
    
    if mau_toi_gian < 0:
        tu_toi_gian = -tu_toi_gian
        mau_toi_gian = -mau_toi_gian

    print(f"Phân số gốc: {tu_so}/{mau_so}")
    print(f"Phân số đã tối giản: {tu_toi_gian}/{mau_toi_gian}")
