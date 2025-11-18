def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

numerator_str = input("Nhập tử số: ")
denominator_str = input("Nhập mẫu số: ")

if not numerator_str.isdigit() or not denominator_str.isdigit():
    print("Đầu vào không hợp lệ. Vui lòng nhập số nguyên.")
else:
    numerator = int(numerator_str)
    denominator = int(denominator_str)
    if denominator == 0:
        print("Mẫu số không thể bằng 0.")
    else:
        common_divisor = gcd(abs(numerator), abs(denominator))
        simplified_numerator = numerator // common_divisor
        simplified_denominator = denominator // common_divisor
        print(f"Phân số đã tối giản là: {simplified_numerator}/{simplified_denominator}")