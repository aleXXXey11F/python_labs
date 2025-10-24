import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from src.text import tokenize, count_freg, top_n, normalize
import csv
from pathlib import Path

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
    input_path = Path('data/input.txt')     
    output_path = Path("data/report.csv")   

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

if name == "__main__":
    main()