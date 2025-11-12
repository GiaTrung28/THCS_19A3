# Bài 9: Nhập số kWh điện đã tiêu thụ từ bàn phím. Sau đó, tính và in ra tổng số tiền điện phải trả dựa trên công thức sau:
# Bậc 1 (0-100 kWh): 1.678 VND/kWh
# Bậc 2 (101-200 kWh): 1.734 VNĐ/kWh
# Bậc 3 (201-300 kWh): 2.014 VNĐ/kWh
# (chỉ sử dụng kiến thức đã học)

# Giả định dữ liệu nhập vào (ví dụ: 250 kWh)
so_kwh = 250
tong_tien_dien = 0

# Tính toán theo bậc thang (sử dụng cấu trúc if/elif/else)
if so_kwh <= 100:
    tong_tien_dien = so_kwh * 1678
elif so_kwh <= 200:
    # Tính tiền bậc 1
    tong_tien_dien += 100 * 1678
    # Tính tiền bậc 2
    tong_tien_dien += (so_kwh - 100) * 1734
elif so_kwh <= 300:
    # Tính tiền bậc 1 và 2 đầy đủ
    tong_tien_dien += 100 * 1678
    tong_tien_dien += 100 * 1734
    # Tính tiền bậc 3
    tong_tien_dien += (so_kwh - 200) * 2014
else:
    # Mở rộng cho các bậc cao hơn nếu cần, nhưng đề bài chỉ yêu cầu đến 300 kWh.
    # Coi như các kWh vượt quá 300 sẽ tính theo bậc 3 luôn trong ví dụ này.
    tong_tien_dien += 100 * 1678
    tong_tien_dien += 100 * 1734
    tong_tien_dien += (so_kwh - 200) * 2014 # Áp dụng bậc 3 cho phần dư


# In kết quả
print(f"Tổng số tiền điện phải trả cho {so_kwh} kWh là: *{tong_tien_dien}* VND")
