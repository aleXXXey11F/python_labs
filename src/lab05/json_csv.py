import json
import csv
from pathlib import Path


def json_to_csv(src_path: str, dst_path: str) -> None:
    """Конвертирует JSON файл в CSV файл."""
    src = Path(src_path)
    dst = Path(dst_path)
    
    if not src.exists():
        raise FileNotFoundError(f"Source file {src_path} not found")
    
    # Читаем JSON
    try:
        with open(src, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format: {e}")
    
    if not data:
        raise ValueError("JSON file is empty")
    
    # Получаем все ключи из всех объектов
    all_keys = set()
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("JSON should contain array of objects")
        all_keys.update(item.keys())
    
    # Записываем CSV
    with open(dst, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=sorted(all_keys))
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(src_path: str, dst_path: str) -> None:
    """Конвертирует CSV файл в JSON файл."""
    src = Path(src_path)
    dst = Path(dst_path)
    
    if not src.exists():
        raise FileNotFoundError(f"Source file {src_path} not found")
    
    # Читаем CSV
    try:
        with open(src, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)
    except csv.Error as e:
        raise ValueError(f"Invalid CSV format: {e}")
    
    if not data:
        raise ValueError("CSV file is empty")
    
    # Записываем JSON
    with open(dst, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)