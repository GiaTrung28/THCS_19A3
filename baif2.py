def giai_phuong_trinh_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -b / a
        print(f"Nghiệm của phương trình là x = {x}")

giai_phuong_trinh_bac_nhat(2, 4)
giai_phuong_trinh_bac_nhat(0, 5)
giai_phuong_trinh_bac_nhat(0, 0)
