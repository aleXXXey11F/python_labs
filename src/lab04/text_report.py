import sys
import os
from pathlib import Path

# Добавляем путь к папке lib
project_root = Path(__file__).parent.parent.parent.parent
lib_path = project_root / "lib"
sys.path.insert(0, str(lib_path))

try:
    from lib.text import tokenize, count_freg, top_n, normalize
except ImportError as e:
    print(f"Ошибка импорта: {e}")
    print("Убедитесь, что файл lib/text.py существует")
    sys.exit(1)

import csv

table = True

def print_table(top: list[tuple]):
    if not top:
        print('Нет слов для отображения')
        return
    max_len = max(len(word) for word, _ in top)
    col_word = 'слово'
    col_freq = 'частота'

    width_word = max(max_len, len(col_word))
    width_freq = len(col_freq)
    print(f"{col_word:<{width_word}} | {col_freq}")
    print("-" * width_word + "-+-" + "-" * width_freq)

    for word, count in top:
        print(f"{word:<{width_word}} | {count}")


def main():
    # Ищем файл в корневой папке data/input.txt
    input_path = Path(__file__).parent.parent.parent.parent / "data" / "input.txt"     
    output_path = Path(__file__).parent.parent.parent.parent / "data" / "report.csv"   

    if not input_path.exists():
        print(f"Файл {input_path} не найден!")
        sys.exit(1)

    try:
        text = input_path.read_text(encoding="utf-8")
    except UnicodeDecodeError as e:
        print(f"Ошибка кодировки при чтении {input_path}: {e}")
        sys.exit(1) 

    text = normalize(text)
    tokens = tokenize(text)
    freq = count_freg(tokens)

    def sort_key(item):
        word, count = item
        return (-count, word)

    sorted_items = sorted(freq.items(), key=sort_key)
     
     
    output_path.parent.mkdir(parents=True, exist_ok=True)  
    with output_path.open("w", newline="", encoding="utf-8") as file: 
        writer = csv.writer(file) 
        writer.writerow(["word", "count"]) 
        writer.writerows(sorted_items)
    
    total_words = sum(freq.values())
    unique_words = len(freq)
    top5 = top_n(freq, n=5)

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print(f"Топ: {top5}")

    if table:
        print("\nТаблица топ слов:")
        print_table(top5)

if __name__ == "__main__":
    main()