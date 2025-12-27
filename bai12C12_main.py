from bai2C12_chuoi_utility import dao_nguoc_chuoi

chuoi_bat_ky = "hôm nay trời lạnh quá"
chuoi_dao_nguoc = dao_nguoc_chuoi(chuoi_bat_ky)

print(f"Chuỗi gốc: {chuoi_bat_ky}")
print(f"Chuỗi đảo ngược: {chuoi_dao_nguoc}")