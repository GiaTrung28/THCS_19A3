def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1_str = input("Nhập số thứ nhất: ")
num2_str = input("Nhập số thứ hai: ")

if not num1_str.isdigit() or not num2_str.isdigit():
    print("Đầu vào không hợp lệ. Vui lòng nhập số nguyên dương.")
else:
    num1 = int(num1_str)
    num2 = int(num2_str)
    if num1 <= 0 or num2 <= 0:
        print("Vui lòng nhập số nguyên dương.")
    else:
        result = gcd(num1, num2)
        print(f"Ước chung lớn nhất của {num1} và {num2} là: {result}")