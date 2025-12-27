numbers = [10, 20, 30, 40, 50, 60]

with open("so_nguyen.txt", "w") as f:
    for number in numbers:
        f.write(str(number) + "\n")

print("Đã ghi danh sách số nguyên vào tập tin so_nguyen.txt")