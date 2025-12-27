with open("vanban.txt", "r", encoding="utf-8") as f:
    content = f.read()

content = content.lower()
for char in '.,!?;:"':
    content = content.replace(char, "")

words = content.split()

word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print("Tần suất xuất hiện của các từ:")
for word, count in word_freq.items():
    print(f"'{word}': {count} lần")
