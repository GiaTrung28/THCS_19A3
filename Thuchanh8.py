def tim_so_le_lon_nhat(a, b, c):
  so_le_lon_nhat = -1  
  
  if a % 2 != 0:
    so_le_lon_nhat = a
  if b % 2 != 0 and b > so_le_lon_nhat:
    so_le_lon_nhat = b
  if c % 2 != 0 and c > so_le_lon_nhat:
    so_le_lon_nhat = c
    
  return so_le_lon_nhat

print(tim_so_le_lon_nhat(2, 4, 6)) 
