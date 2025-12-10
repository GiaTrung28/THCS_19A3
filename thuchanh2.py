def giai_phuong_trinh_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -b / a
        print(f"Phương trình có nghiệm duy nhất x = {x}")

#Ví dụ
giai_phuong_trinh_bac_nhat(2,8)
giai_phuong_trinh_bac_nhat(99,100)