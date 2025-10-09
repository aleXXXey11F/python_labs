def format_record(rec: tuple[str, str, float]) -> str:
    if not isinstance(rec[0], str) or not isinstance(rec[1], str) or not isinstance(rec[2], (int, float)):
        raise TypeError("Неверные типы данных в записи")
    
    fio, group, gpa = rec
    
    if not fio.strip():
        raise ValueError("ФИО не может быть пустым")
    if not group.strip():
        raise ValueError("Группа не может быть пустой")
    if gpa < 0:
        raise ValueError("GPA не может быть отрицательным")
    
    fio_parts = ' '.join(fio.split()).title().split()
    
    initials = []
    for part in fio_parts[1:]:  
        if part:  
            initials.append(part[0].upper() + '.')
    
    formatted_fio = f"{fio_parts[0]} {' '.join(initials)}"
    
    formatted_gpa = f"{gpa:.2f}"
    
    return f"{formatted_fio}, гр. {group.strip()}, GPA {formatted_gpa}"

test_cases = [
    ("Иванов Иван Иванович", "BIVT-25", 4.6),
    ("Петров Пётр", "IKBO-12", 5.0),
    ("Петров Пётр Петрович", "IKBO-12", 5.0),
    ("  сидорова  анна   сергеевна ", "ABB-01", 3.999),
]

print("Тест-кейсы:")
for i, test_case in enumerate(test_cases, 1):
    try:
        result = format_record(test_case)
        print(f"{i}. {result}")
    except (ValueError, TypeError) as e:
        print(f"{i}. Ошибка: {e}")

print("\nНекорректные записи:")
invalid_cases = [
    ("", "BIVT-25", 4.6),  
    ("Иванов Иван", "", 4.6),  
    ("Иванов Иван", "BIVT-25", -1.0),  
    ("Иванов Иван", "BIVT-25", "4.6"),  
]

for i, test_case in enumerate(invalid_cases, 1):
    try:
        result = format_record(test_case)
        print(f"{i}. {result}")
    except (ValueError, TypeError) as e:
        print(f"{i}. Ошибка: {e}")