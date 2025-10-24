import re
from typing import Dict, List, Tuple


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not text:
        return ""
    result = text
    if yo2e:
        result = result.replace('ё', 'е').replace('Ё', 'Е')
    if casefold:
        result = result.casefold()
    control_chars = ['\t', '\r', '\n']
    for char in control_chars:
        result = result.replace(char, ' ')
    result = re.sub(r'\s+', ' ', result).strip()

    return result


def tokenize(text: str) -> List[str]:
    if not text:
        return []
    pattern = r'\w+(?:-\w+)*'
    tokens = re.findall(pattern, text)
    return tokens

def count_freq(tokens: List[str]) -> Dict[str, int]:
    freq_dict = {}
    for token in tokens:
        freq_dict[token] = freq_dict.get(token, 0) + 1
    
    return freq_dict


def top_n(freq: Dict[str, int], n: int = 5) -> List[Tuple[str, int]]:
    if not freq:
        return []
    items = list(freq.items())
    sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]
"""
# Тесты для normalize
print("=== normalize ===")
print(repr(normalize("ПрИвЕт\nМИр\t")))  
print(repr(normalize("ёжик, Ёлка", yo2e=True)))  
print(repr(normalize("Hello\r\nWorld")))  
print(repr(normalize("  двойные   пробелы  ")))  

# Тесты для tokenize
print("\n=== tokenize ===")
print(tokenize("привет мир"))  
print(tokenize("hello,world!!!"))  
print(tokenize("по-настоящему круто"))  
print(tokenize("2025 год"))  
print(tokenize("emoji 😀 не слово"))  

# Тесты для count_freq + top_n
print("\n=== count_freq + top_n ===")
tokens1 = ["a", "b", "a", "c", "b", "a"]
freq1 = count_freq(tokens1)
print(freq1)  
print(top_n(freq1, 2))  

tokens2 = ["bb", "aa", "bb", "aa", "cc"]
freq2 = count_freq(tokens2)
print(freq2)  
print(top_n(freq2, 2))  
"""


"""
# ТЕСТЫ ДЛЯ ЗАДАНИЯ A
if __name__ == "__main__":
    # normalize
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"
    
    # tokenize
    assert tokenize("привет, мир!") == ["привет", "мир"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]
    
    # count_freq + top_n
    freq = count_freq(["a","b","a","c","b","a"])
    assert freq == {"a":3, "b":2, "c":1}
    assert top_n(freq, 2) == [("a",3), ("b",2)]
    
    # тай-брейк по слову при равной частоте
    freq2 = count_freq(["bb","aa","bb","aa","cc"])
    assert top_n(freq2, 2) == [("aa",2), ("bb",2)]
    
    print("✅ Все тесты прошли успешно!")
    """