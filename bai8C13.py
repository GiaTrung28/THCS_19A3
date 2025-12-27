import os

def manipulate_files():
    temp_dir = "temp_files"
    os.makedirs(temp_dir, exist_ok=True)
    
    file_path = os.path.join(temp_dir, "file.txt")
    open(file_path, "a").close()
    
    new_file_path = os.path.join(temp_dir, "new_file.txt")
    os.rename(file_path, new_file_path)
    
    current_dir_file_path = "new_file.txt"
    os.rename(new_file_path, current_dir_file_path)
    
    os.rmdir(temp_dir)
    print(f"Đã di chuyển 'new_file.txt' ra thư mục hiện tại và xóa thư mục '{temp_dir}'.")

manipulate_files()