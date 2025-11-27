import sys
from pathlib import Path

# Добавляем путь к модулям
sys.path.append(str(Path(__file__).parent / 'src'))

from lab05.json_csv import json_to_csv, csv_to_json
from lab05.csv_xlsx import csv_to_xlsx

def main():
    print("Демонстрация работы модулей lab05")
    
    # Создаем директории для выходных файлов
    output_dir = Path("data/out")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # 1. JSON → CSV
        print("\n1. Конвертация JSON → CSV:")
        json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
        print(" Успешно: data/out/people_from_json.csv")
        
        # 2. CSV → JSON
        print("\n2. Конвертация CSV → JSON:")
        csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
        print(" Успешно: data/out/people_from_csv.json")
        
        # 3. CSV → XLSX
        print("\n3. Конвертация CSV → XLSX:")
        csv_to_xlsx("data/samples/cities.csv", "data/out/cities.xlsx")
        print(" Успешно: data/out/cities.xlsx")
        
        # 4. Обратная проверка: JSON → CSV → JSON
        print("\n4. Обратная проверка JSON → CSV → JSON:")
        json_to_csv("data/out/people_from_csv.json", "data/out/people_roundtrip.csv")
        csv_to_json("data/out/people_roundtrip.csv", "data/out/people_roundtrip.json")
        print(" Успешно: data/out/people_roundtrip.json")
        
        print("\n Все операции выполнены успешно!")
        
    except Exception as e:
        print(f" Ошибка: {e}")

if __name__ == "__main__":
    main()