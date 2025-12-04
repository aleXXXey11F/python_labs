from src.lab08.models import Student
from src.lab08.serialize import students_to_json, students_from_json
import sys

def main():
    """Основная функция для демонстрации работы."""
    
    print("=== Лабораторная работа 8: ООП в Python ===")
    print()
    
    # Создаем список студентов
    students = [
        Student(
            fio="Иванов Иван Иванович",
            birthdate="2000-05-15",
            group="SE-01",
            gpa=4.5
        ),
        Student(
            fio="Петрова Анна Сергеевна",
            birthdate="2001-08-22",
            group="CS-02",
            gpa=4.8
        ),
        Student(
            fio="Сидоров Алексей Петрович",
            birthdate="1999-12-03",
            group="AI-03",
            gpa=3.9
        )
    ]
    
    print("Создано студентов:", len(students))
    print()
    
    # Демонстрация методов
    print("Информация о студентах:")
    print("-" * 50)
    for i, student in enumerate(students, 1):
        print(f"{i}. {student}")
        print(f"   Год рождения: {student.birth_year}")
        print(f"   Словарь: {student.to_dict()}")
        print()
    
    # Сохраняем в JSON
    output_path = "data/lab08/students_output.json"
    try:
        students_to_json(students, output_path)
        print(f"Данные сохранены в: {output_path}")
    except Exception as e:
        print(f"Ошибка сохранения: {e}")
        sys.exit(1)
    
    print()
    
    # Загружаем из JSON
    try:
        loaded_students = students_from_json(output_path)
        print(f"Загружено студентов: {len(loaded_students)}")
        
        print()
        print("Загруженные студенты:")
        print("-" * 50)
        for i, student in enumerate(loaded_students, 1):
            print(f"{i}. {student}")
            
    except Exception as e:
        print(f"Ошибка загрузки: {e}")
        sys.exit(1)
    
    print()
    
    # Демонстрация валидации
    print("Тестирование валидации:")
    print("-" * 50)
    
    try:
        # Неверный формат даты
        Student(fio="Тестовый Студент", birthdate="15-05-2000", group="TEST", gpa=4.0)
        print("ОШИБКА: Должна быть вызвана ошибка валидации даты")
    except ValueError as e:
        print(f"✓ Корректно обработана ошибка даты: {e}")
    
    try:
        # GPA вне диапазона
        Student(fio="Тестовый Студент", birthdate="2000-05-15", group="TEST", gpa=6.0)
        print("ОШИБКА: Должна быть вызвана ошибка валидации GPA")
    except ValueError as e:
        print(f"✓ Корректно обработана ошибка GPA: {e}")
    
    try:
        # Неполное ФИО
        Student(fio="Иванов", birthdate="2000-05-15", group="TEST", gpa=4.0)
        print("ОШИБКА: Должна быть вызвана ошибка валидации ФИО")
    except ValueError as e:
        print(f"✓ Корректно обработана ошибка ФИО: {e}")
    
    print()
    print("=== Работа завершена успешно ===")

if __name__ == "__main__":
    main()