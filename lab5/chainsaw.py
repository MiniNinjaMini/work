import json
data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

with open("users.jsonl", "w", encoding="utf-8") as file:
    for item in data:
        file.write(json.dumps(item, ensure_ascii=False) + "\n")


def find_lines_with_word(filename, word):
    with open(filename, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if word in line]  # Фильтруем строки

    return lines

filename = "row.txt"
word = "Филиал" 
found_lines = find_lines_with_word(filename, word)

if found_lines:
    print("Найденные строки:")
    for line in found_lines:
        data.append(3)=line[11:]
else:
    print(f"Слово '{word}' не найдено в файле.")
