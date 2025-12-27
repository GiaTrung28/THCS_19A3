import os

def create_project_structure():
    base_dir = "my_project"
    src_dir = os.path.join(base_dir, "src")
    docs_dir = os.path.join(base_dir, "docs")
    data_dir = os.path.join(base_dir, "data")

    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(docs_dir, exist_ok=True)
    os.makedirs(data_dir, exist_ok=True)
    
    open(os.path.join(src_dir, "main.py"), "a").close()
    open(os.path.join(docs_dir, "README.md"), "a").close()
    open(os.path.join(data_dir, "input.txt"), "a").close()
    
    print(f"Cấu trúc thư mục của '{base_dir}':")
    for root, dirs, files in os.walk(base_dir):
        level = root.replace(base_dir, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{subindent}{f}')

create_project_structure()
