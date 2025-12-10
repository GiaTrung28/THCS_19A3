def kiem_tra_so_armstrong(n):
  """
  Kiểm tra số nguyên dương n có phải là số Armstrong (bậc 3) hay không.
  """
  str_n = str(n)
  tong_lap_phuong = 0
  for chu_so in str_n:
    tong_lap_phuong += int(chu_so) ** 3

  return tong_lap_phuong == n

print(kiem_tra_so_armstrong(153))  