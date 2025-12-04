#!/usr/bin/env python3
"""
Демонстрационный скрипт для ЛР9 - Класс Group и CRUD операции
"""

import sys
import os

# Добавляем путь для импорта
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from lab08.models import Student
from lab09.group import Group


def demonstrate_crud_operations():
    """Демонстрация CRUD операций."""
    print("="*60)
    print("ДЕМОНСТРАЦИЯ CRUD ОПЕРАЦИЙ")
    print("="*60)
    
    # Создаем группу студентов
    csv_path = "data/lab09/students.csv"
    group = Group(csv_path)
    
    print(f"\n1. Инициализация группы:")
    print(f"   Файл: {csv_path}")
    print(f"   Студентов в базе: {len(group)}")
    
    print(f"\n2. Вывод всех студентов:")
    print("-" * 70)
    students = group.list()
    for i, student in enumerate(students, 1):
        print(f"{i:2}. {student}")
    print("-" * 70)
    
    print(f"\n3. Добавление нового студента:")
    new_student = Student(
        fio="Новиков Павел Сергеевич",
        birthdate="2001-04-18",
        group="SE-03",
        gpa=4.1
    )
    try:
        group.add(new_student)
        print(f"   Добавлен: {new_student}")
    except ValueError as e:
        print(f"   Ошибка: {e}")
    
    print(f"\n4. Поиск студентов (подстрока 'Петр'):")
    found = group.find("Петр")
    for i, student in enumerate(found, 1):
        print(f"   {i}. {student}")
    
    print(f"\n5. Обновление студента:")
    try:
        if group.update("Иванов Иван Иванович", gpa=4.7, group="SE-01A"):
            print("   GPA Иванова Ивана обновлен до 4.7")
            print("   Группа изменена на SE-01A")
    except ValueError as e:
        print(f"   Ошибка обновления: {e}")
    
    print(f"\n6. Статистика по группе:")
    try:
        stats = group.stats()
        print(f"   Всего студентов: {stats['count']}")
        print(f"   Минимальный GPA: {stats['min_gpa']:.2f}")
        print(f"   Максимальный GPA: {stats['max_gpa']:.2f}")
        print(f"   Средний GPA: {stats['avg_gpa']:.2f}")
        print(f"   Распределение по группам:")
        for group_name, count in stats['groups'].items():
            print(f"     - {group_name}: {count} студентов")
        print(f"   Топ-5 студентов:")
        for i, top_student in enumerate(stats['top_5_students'], 1):
            print(f"     {i}. {top_student['fio']} (GPA: {top_student['gpa']:.2f})")
    except ValueError as e:
        print(f"   Ошибка статистики: {e}")
    
    print(f"\n7. Удаление студента:")
    if group.remove("Сидоров Алексей Петрович"):
        print("   Сидоров Алексей удален")
    else:
        print("   Студент не найден")
    
    print(f"\n8. Финальный список студентов:")
    print("-" * 70)
    final_students = group.list()
    for i, student in enumerate(final_students, 1):
        print(f"{i:2}. {student}")
    print("-" * 70)
    print(f"   Всего студентов: {len(final_students)}")


def demonstrate_error_handling():
    """Демонстрация обработки ошибок."""
    print("\n" + "="*60)
    print("ДЕМОНСТРАЦИЯ ОБРАБОТКИ ОШИБОК")
    print("="*60)
    
    # Создаем тестовую группу
    test_csv = "data/lab09/test_students.csv"
    group = Group(test_csv)
    
    print("\n1. Попытка добавить студента с существующим ФИО:")
    student1 = Student(
        fio="Дубль Тест Тестович",
        birthdate="2000-01-01",
        group="TEST-01",
        gpa=4.0
    )
    student2 = Student(
        fio="Дубль Тест Тестович",  # То же ФИО!
        birthdate="2001-02-02",
        group="TEST-02",
        gpa=3.5
    )
    
    try:
        group.add(student1)
        print("   Первый студент добавлен успешно")
    except ValueError as e:
        print(f"   Ошибка: {e}")
    
    try:
        group.add(student2)
        print("   Второй студент добавлен успешно")
    except ValueError as e:
        print(f"   Ошибка при добавлении дубля: {e}")
    
    print("\n2. Попытка обновления несуществующего студента:")
    if not group.update("Несуществующий Студент", gpa=5.0):
        print("   Корректно: студент не найден для обновления")
    
    print("\n3. Попытка обновления с некорректными данными:")
    try:
        group.update("Дубль Тест Тестович", gpa=6.0)  # GPA > 5
        print("   ОШИБКА: Должна быть вызвана ошибка валидации")
    except ValueError as e:
        print(f"   Корректно: {e}")
    
    print("\n4. Попытка удаления несуществующего студента:")
    if not group.remove("Нет Такого Студента"):
        print("   Корректно: студент не найден для удаления")
    
    # Удаляем тестовый файл
    import os
    if os.path.exists(test_csv):
        os.remove(test_csv)
        print(f"\n   Тестовый файл удален: {test_csv}")


def demonstrate_import_export():
    """Демонстрация импорта/экспорта."""
    print("\n" + "="*60)
    print("ДЕМОНСТРАЦИЯ ИМПОРТА/ЭКСПОРТА")
    print("="*60)
    
    # Создаем тестовую группу
    test_csv = "data/lab09/import_export_test.csv"
    group = Group(test_csv)
    
    print("\n1. Импорт из JSON (данные из ЛР8):")
    json_path = "data/lab08/students_output.json"
    if os.path.exists(json_path):
        imported_count = group.import_from_json(json_path)
        print(f"   Импортировано студентов: {imported_count}")
    else:
        print(f"   JSON файл не найден: {json_path}")
        print("   Создаем тестовых студентов...")
        # Создаем несколько тестовых студентов
        test_students = [
            Student("Импортный Студент 1", "2000-01-01", "IMP-01", 4.0),
            Student("Импортный Студент 2", "2001-02-02", "IMP-02", 4.5),
            Student("Импортный Студент 3", "2002-03-03", "IMP-03", 3.8),
        ]
        for student in test_students:
            try:
                group.add(student)
            except ValueError:
                pass
    
    print("\n2. Экспорт в JSON:")
    export_path = "data/lab09/exported_students.json"
    group.export_to_json(export_path)
    if os.path.exists(export_path):
        file_size = os.path.getsize(export_path)
        print(f"   Экспортировано в: {export_path}")
        print(f"   Размер файла: {file_size} байт")
    
    print("\n3. Очистка базы данных:")
    group.clear()
    print(f"   Студентов после очистки: {len(group)}")
    
    # Удаляем тестовые файлы
    if os.path.exists(test_csv):
        os.remove(test_csv)
    if os.path.exists(export_path):
        os.remove(export_path)
    print(f"   Тестовые файлы удалены")


def main():
    """Основная функция."""
    print("="*60)
    print("ЛАБОРАТОРНАЯ РАБОТА 9: База данных на CSV")
    print("Класс Group, CRUD-операции")
    print("="*60)
    
    # Создаем директории для данных
    os.makedirs("data/lab09", exist_ok=True)
    
    # Демонстрируем различные аспекты
    demonstrate_crud_operations()
    demonstrate_error_handling()
    demonstrate_import_export()
    
    print("\n" + "="*60)
    print("ВСЕ ТЕСТЫ ЗАВЕРШЕНЫ УСПЕШНО!")
    print("="*60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем.")
        sys.exit(1)
    except Exception as e:
        print(f"\nНеожиданная ошибка: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)