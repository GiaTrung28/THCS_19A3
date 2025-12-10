def kiem_tra_so_doi_xung(n):
    chuoi_so = str(n)
    return chuoi_so == chuoi_so[::-1]

print(f"Số 121 có phải số đối xứng không? {kiem_tra_so_doi_xung(121)}")
print(f"Số 353 có phải số đối xứng không? {kiem_tra_so_doi_xung(353)}")
print(f"Số 123 có phải số đối xứng không? {kiem_tra_so_doi_xung(123)}")
