# Bài 7: Nhập tên đăng nhập và mật khẩu từ bàn phím. Kiểm tra quyền truy cập nếu tên đăng nhập là "admin" và mật khẩu không phải "password123" (chỉ sử dụng kiến thức đã học).

# Giả định dữ liệu nhập vào (ví dụ 1 - được phép truy cập)
ten_dang_nhap_1 = "admin"
mat_khau_1 = "matkhaukhac"

# Giả định dữ liệu nhập vào (ví dụ 2 - không được phép)
ten_dang_nhap_2 = "admin"
mat_khau_2 = "password123"

# Kiểm tra quyền truy cập cho ví dụ 1
duoc_phep_1 = (ten_dang_nhap_1 == "admin") and (mat_khau_1 != "password123")

# Kiểm tra quyền truy cập cho ví dụ 2
duoc_phep_2 = (ten_dang_nhap_2 == "admin") and (mat_khau_2 != "password123")


# In kết quả
if duoc_phep_1:
    print(f"Ví dụ 1: *Được cấp quyền truy cập*")
else:
    print(f"Ví dụ 1: *Không được cấp quyền truy cập*")

if duoc_phep_2:
    print(f"Ví dụ 2: *Được cấp quyền truy cập*")
else:
    print(f"Ví dụ 2: *Không được cấp quyền truy cập*")
