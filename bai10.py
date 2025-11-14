
luong_co_ban = float(input("Nhập mức lương cơ bản (VNĐ): "))
so_ngay_cong = int(input("Nhập số ngày công trong tháng: "))

luong_mot_ngay = luong_co_ban / 22

tong_luong = luong_mot_ngay * so_ngay_cong

if so_ngay_cong > 22:
    tien_thuong = tong_luong * 0.10
    tong_luong += tien_thuong
    print(f"Bạn được thưởng thêm {tien_thuong:,.0f} VNĐ.")
elif so_ngay_cong < 22:
    tien_phat = tong_luong * 0.05
    tong_luong -= tien_phat
    print(f"Bạn bị phạt {tien_phat:,.0f} VNĐ.")
else:
    print("Bạn làm việc đủ ngày công, không có thưởng phạt.")

print(f"Tổng tiền lương thực nhận của nhân viên là: {tong_luong:,.0f} VNĐ")
