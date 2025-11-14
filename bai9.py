so_kwh = float(input("Nhập số kWh điện đã tiêu thụ: "))

tong_tien = 0

if so_kwh <= 100:
    tong_tien = so_kwh * 1678
elif so_kwh <= 200:
    tong_tien = (100 * 1678) + ((so_kwh - 100) * 1734)
elif so_kwh <= 300:
    tong_tien = (100 * 1678) + (100 * 1734) + ((so_kwh - 200) * 2014)

print(f"Tổng số tiền điện phải trả là: {tong_tien:,.0f} VNĐ")