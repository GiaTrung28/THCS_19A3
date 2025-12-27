import csv

data = [
    ['ID', 'Tên', 'Lương'],
    ['1', 'Nguyen Van A', '60000'],
    ['2', 'Le Thi B', '45000'],
    ['3', 'Tran Van C', '75000'],
    ['4', 'Pham Thi D', '50000']
]

with open('nhan_vien.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Nhân viên có mức lương trên 50000:")
with open('nhan_vien.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row['Lương']) > 50000:
            print(f"ID: {row['ID']}, Tên: {row['Tên']}, Lương: {row['Lương']}")