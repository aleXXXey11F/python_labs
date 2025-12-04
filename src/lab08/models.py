from dataclasses import dataclass, field
from datetime import datetime, date
from typing import Optional
import re

@dataclass
class Student:
    """Класс для представления студента с валидацией данных."""
    
    fio: str
    birthdate: str
    group: str
    gpa: float
    
    def __post_init__(self):
        """Валидация данных после инициализации объекта."""
        # Валидация формата даты
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Неверный формат даты: {self.birthdate}. Ожидается YYYY-MM-DD")
        
        # Валидация диапазона GPA
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"GPA должен быть в диапазоне от 0 до 5. Получено: {self.gpa}")
        
        # Валидация ФИО (должно содержать хотя бы пробел)
        if ' ' not in self.fio.strip():
            raise ValueError(f"ФИО должно содержать имя и фамилию. Получено: {self.fio}")
    
    def age(self) -> int:
        """
        Возвращает возраст студента в полных годах.
        
        Returns:
            int: Возраст студента
        """
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        
        age = today.year - birth_date.year
        
        # Проверяем, был ли уже день рождения в этом году
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
            
        return age
    
    def to_dict(self) -> dict:
        """
        Сериализует объект Student в словарь.
        
        Returns:
            dict: Словарь с данными студента
        """
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Student':
        """
        Десериализует словарь в объект Student.
        
        Args:
            data (dict): Словарь с данными студента
            
        Returns:
            Student: Объект Student
        """
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"]
        )
    
    def __str__(self) -> str:
        """
        Возвращает строковое представление студента.
        
        Returns:
            str: Строка с информацией о студенте
        """
        return f"{self.fio} ({self.group}), GPA: {self.gpa:.2f}, возраст: {self.age()} лет"
    
    @property
    def birth_year(self) -> int:
        """Возвращает год рождения студента."""
        return int(self.birthdate.split('-')[0])
    