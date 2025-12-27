from du_lieu.bai4C12_danh_sach import sap_xep_tang_dan
from du_lieu.bai4C12_tu_dien import lay_gia_tri

danh_sach_so = [5, 2, 9, 1, 5, 6]
print(f"Danh sách gốc: {danh_sach_so}")
danh_sach_sap_xep = sap_xep_tang_dan(danh_sach_so)
print(f"Danh sách sắp xếp tăng dần: {danh_sach_sap_xep}")

my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
khoa_can_tim = 'banana'
gia_tri = lay_gia_tri(my_dict, khoa_can_tim)
print(f"Giá trị của khóa '{khoa_can_tim}' là: {gia_tri}")
