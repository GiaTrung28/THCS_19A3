def nhom_sinh_vien_theo_diem(diem_sinh_vien):
    
    nhom_theo_diem = {}
    for ten, diem in diem_sinh_vien.items():
        if diem in nhom_theo_diem:
            nhom_theo_diem[diem].append(ten)
        else:
            nhom_theo_diem[diem] = [ten]
            
    return nhom_theo_diem

student_scores_19 = {
    'An': 8.5,
    'Binh': 9.0,
    'Chau': 7.0,
    'Duc': 8.5,
    'Tam': 9.0
}
grouped_scores = nhom_sinh_vien_theo_diem(student_scores_19)
print(f"Dictionary điểm số gốc: {student_scores_19}")
print(f"Dictionary nhóm theo điểm: {grouped_scores}")
