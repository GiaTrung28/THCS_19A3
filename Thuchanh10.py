def tim_so_fibonacci(n):
  
  if n <= 1:
    return n
  else:
    return tim_so_fibonacci(n - 1) + tim_so_fibonacci(n - 2)

print(tim_so_fibonacci(0))
print(tim_so_fibonacci(1)) 

