def tinh_s1(n):
    return n * (n + 1) // 2

def tinh_s2(n):
    if n == 0:
        return 1
    tich = 1
    for i in range(1, n):
        tich *= i
    return tich

def tinh_s3(n):
    tong = 0
    for i in range(1, n + 1):
        tong += ((-1)**(i+1)) / i
    return tong

def tinh_s4(n):
    tong = 0
    for k in range(0, n + 1):
        tong += k / (k + 2)
    return tong

n = int(input("Nhập n: "))

print("S1 =", tinh_s1(n))
print("S2 =", tinh_s2(n))
print("S3 =", tinh_s3(n))
print("S4 =", tinh_s4(n))