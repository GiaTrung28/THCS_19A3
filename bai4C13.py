content = """ID,Tên sản phẩm,Giá
1,Laptop,1200
2,Chuột máy tính,25
3,Bàn phím,75"""

with open("san_pham.txt", "w", encoding="utf-8") as f:
    f.write(content)

product_id_to_update = input("Nhập ID của sản phẩm cần cập nhật giá: ")

new_price = input("Nhập giá mới: ")

updated_lines = []
with open("san_pham.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        if line.startswith(product_id_to_update + ","):
            parts = line.strip().split(",")
            parts[-1] = new_price 
            updated_lines.append(",".join(parts) + "\n")
        else:
            updated_lines.append(line)

with open("san_pham.txt", "w", encoding="utf-8") as f:
    f.writelines(updated_lines)

print(f"Đã cập nhật giá sản phẩm ID {product_id_to_update} thành {new_price}")
