#!/usr/bin/env python3
"""
CLI-утилиты для работы с текстом
"""

import argparse
import sys
import os

# Добавляем путь к корню проекта для импорта модулей
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../..'))

from src.lib.io_helpers import read_file, write_file
from src.lab03.text_analysis import calculate_word_frequency, get_top_words

def cat_command(input_file, number_lines=False):
    """
    Реализация команды cat - вывод содержимого файла
    """
    try:
        content = read_file(input_file)
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            if number_lines:
                print(f"{i:6d}\t{line}")
            else:
                print(line)
                
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        sys.exit(1)

def stats_command(input_file, top_n=5):
    """
    Реализация команды stats - анализ частот слов
    """
    try:
        content = read_file(input_file)
        if not content.strip():
            print("Файл пуст")
            return
            
        frequency = calculate_word_frequency(content)
        top_words = get_top_words(frequency, top_n)
        
        print(f"Топ-{top_n} самых частых слов в файле '{input_file}':")
        print("-" * 40)
        for i, (word, count) in enumerate(top_words, 1):
            print(f"{i:2d}. {word:<15} {count:>4} раз")
            
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при анализе текста: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="CLI-утилиты для работы с текстом",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")

    # Подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Входной файл")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # Подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Анализ частот слов")
    stats_parser.add_argument("--input", required=True, help="Входной текстовый файл")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество топ-слов (по умолчанию: 5)")

    args = parser.parse_args()

    if args.command == "cat":
        cat_command(args.input, args.n)
    elif args.command == "stats":
        stats_command(args.input, args.top)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()