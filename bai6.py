nam = int(input("Nhập một năm: "))

if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
    print(f"Năm {nam} là năm nhuận.")
else:
    print(f"Năm {nam} không phải là năm nhuận.")