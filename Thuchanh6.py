import math

def la_so_nguyen_to(n):
  if n <= 1:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

def in_so_nguyen_to_trong_khoang(a, b):
  print(f"Các số nguyên tố trong khoảng [{a}, {b}]:")
  for so in range(a, b + 1):
    if la_so_nguyen_to(so):
      print(so)

