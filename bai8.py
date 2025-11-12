# Bài 8: Nhập cân nặng (kg) và chiều cao (mét). Tính chỉ số BMI theo công thức BMI = cân nặng / (chiều cao * chiều cao). In kết quả BMI ra màn hình, làm tròn đến 2 chữ số thập phân.

# Giả định dữ liệu nhập vào (ví dụ)
can_nang_kg = 60.0
chieu_cao_m = 1.70

# Tính toán BMI
chi_so_bmi = can_nang_kg / (chieu_cao_m * chieu_cao_m)

# In kết quả đã làm tròn
print(f"Chỉ số BMI của bạn là: *{round(chi_so_bmi, 2)}*")
