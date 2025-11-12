# Bài 6: Nhập một năm từ bàn phím. Kiểm tra xem năm đó có phải là năm nhuận không (chia hết cho 400 hoặc chia hết cho 4 nhưng không chia hết cho 100) (chỉ sử dụng kiến thức đã học).

# Giả định dữ liệu nhập vào (ví dụ)
nam_can_kiem_tra = 2024

# Kiểm tra điều kiện năm nhuận
la_nam_nhuan = (nam_can_kiem_tra % 400 == 0) or ((nam_can_kiem_tra % 4 == 0) and (nam_can_kiem_tra % 100 != 0))

# In kết quả
if la_nam_nhuan:
    print(f"Năm *{nam_can_kiem_tra}* là năm nhuận.")
else:
    print(f"Năm *{nam_can_kiem_tra}* không phải là năm nhuận.")
