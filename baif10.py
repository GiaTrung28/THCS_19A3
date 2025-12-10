def tim_so_fibonacci(n):
    if n <= 1:
        return n
    else:
        return tim_so_fibonacci(n - 1) + tim_so_fibonacci(n - 2)

vi_tri_n = 10
so_fib = tim_so_fibonacci(vi_tri_n)
print(f"Số Fibonacci thứ {vi_tri_n} là: {so_fib}")
