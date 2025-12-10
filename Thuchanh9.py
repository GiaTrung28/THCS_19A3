def tinh_tong_chu_so_de_quy(n):
  if n < 10:
    return n
  else:
    return n % 10 + tinh_tong_chu_so_de_quy(n // 10)

print(tinh_tong_chu_so_de_quy(123)) 