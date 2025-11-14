
tien_gui_ban_dau = float(input("Nhập số tiền gửi ban đầu (VNĐ): "))
lai_suat_nam = float(input("Nhập lãi suất hàng năm (%): ")) / 100 


lai_1_thang = tien_gui_ban_dau * lai_suat_nam * (1/12)

lai_2_quy = tien_gui_ban_dau * lai_suat_nam * (2/4)

lai_3_nam = tien_gui_ban_dau * lai_suat_nam * 3

print(f"Số tiền lãi nhận được sau 1 tháng: {lai_1_thang:,.0f} VNĐ")
print(f"Số tiền lãi nhận được sau 2 quý: {lai_2_quy:,.0f} VNĐ")
print(f"Số tiền lãi nhận được sau 3 năm: {lai_3_nam:,.0f} VNĐ")
