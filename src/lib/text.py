import re
from collections import Counter
from typing import Dict, List, Tuple


def normalize(text: str) -> str:
    """Приводит текст к нижнему регистру и нормализует пробелы."""
    if not text:
        return ""

    # Приводим к нижнему регистру
    text = text.lower()

    # Заменяем букву "ё" на "е"
    text = text.replace("ё", "е")

    # Заменяем все пробельные символы на обычные пробелы
    text = re.sub(r"\s+", " ", text)

    # Убираем пробелы в начале и конце
    return text.strip()


def tokenize(text: str) -> List[str]:
    """Разбивает текст на слова (токены)."""
    if not text:
        return []

    # Используем регулярное выражение для извлечения слов
    tokens = re.findall(r"\b[а-яa-z]+\b", text, re.IGNORECASE)
    return tokens


def count_freq(tokens: List[str]) -> Dict[str, int]:
    """Подсчитывает частоту встречаемости токенов."""
    if not tokens:
        return {}

    return dict(Counter(tokens))


def top_n(freq: Dict[str, int], n: int) -> List[Tuple[str, int]]:
    """Возвращает n самых частых токенов с сортировкой по частоте и алфавиту."""
    if not freq or n <= 0:
        return []

    # Сортируем сначала по убыванию частоты, затем по возрастанию слова
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    return sorted_items[:n]
