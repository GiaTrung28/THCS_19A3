n_str = input("Nhập một số nguyên dương n: ")

if not n_str.isdigit():
    print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên dương.")
else:
    n = int(n_str)
    if n <= 2:
        print(f"Không có số nguyên tố nào nhỏ hơn {n}.")
    else:
        is_p = [True] * n
        is_p[0] = is_p[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_p[i]:
                for multiple in range(i*i, n, i):
                    is_p[multiple] = False
        primes = [i for i, p in enumerate(is_p) if p]
        print(f"Các số nguyên tố nhỏ hơn {n} là: {primes}")