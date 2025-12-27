source_file = "vanban.txt" 
destination_file = "vanban_copy.txt"

try:
    with open(source_file, 'rb') as f_source:
        with open(destination_file, 'wb') as f_dest:
            while True:
                chunk = f_source.read(1024) 
                if not chunk:
                    break 
                f_dest.write(chunk)
    print(f"Đã sao chép tập tin từ '{source_file}' sang '{destination_file}' thành công.")
except FileNotFoundError:
    print(f"Lỗi: Tập tin nguồn '{source_file}' không tồn tại.")