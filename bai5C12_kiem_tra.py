import sys
import os

current_dir = os.path.dirname(os.path.abspath("thu_vien_chung"))
parent_dir = os.path.dirname(current_dir)
thu_vien_chung_path = os.path.join(parent_dir, 'thu_vien_chung')
sys.path.append(thu_vien_chung_path)

try:
    import thu_vien_chung
    number_to_check = 17
    if thu_vien_chung.kiem_tra_so_nguyen_to(number_to_check):
        print(f"{number_to_check} là số nguyên tố.")
    else:
        print(f"{number_to_check} không phải là số nguyên tố.")
except ImportError:
    print("Không thể import module xu_ly_so. Vui lòng kiểm tra đường dẫn.")