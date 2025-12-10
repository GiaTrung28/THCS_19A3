import math

def la_so_nguyen_to(n):
  
  if n <= 1:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

print("Các số nguyên tố trong khoảng [100, 500]:")
for so in range(100, 501):
    if la_so_nguyen_to(so):
        print(so)
