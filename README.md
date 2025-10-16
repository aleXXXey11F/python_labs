# python_labs

# Лабораторная работа 1
## Задание 1
![скриншот задания 1](images/lab01/img01.png)
## Задание 2
![скриншот задания 2](images/lab01/img02.png)
## Задание 3
![скриншот задания 3](images/lab01/img03.png)
## Задание 4
![скриншот задания 4](images/lab01/img04.png)
## Задание 5
![скриншот задания 5](images/lab01/img05.png)
## Задание 6
![скриншот задания 6](images/lab01/img06.png)
## Задание 7
![скриншот задания 7](images/lab01/img07.png)
# Лабораторная работа 2
## Задание 1 - Arrays
    nums=[1.0, 1, 2.5, 2.5, 0]
    def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
        if not nums:
            raise ValueError("Список не может быть пустым")
        else:
            minmax=(min(nums),max(nums))
            return minmax
    def unique_sorted(nums: list[float | int]) -> list[float | int]:
        dict_nums=dict.fromkeys(nums)
        nums_un=list(dict_nums)
        nums_un.sort()
        return nums_un
    def flatten(mat: list[list | tuple]) -> list:
        result = []
        for row in mat:
            if not isinstance(row, (list, tuple)):
                raise TypeError("Ожидался список или кортеж")
            result.extend(row)
        return result 
    
    try:      
        print(min_max(nums))
    except ValueError as e:
        print(f"Ошибка: {e}") #min_max output
    
    print(unique_sorted(nums)) #unique_sorted output
    
    try:
        print(flatten(nums))
    except TypeError as a:
        print(f"Ошибка: {a}") #flatten output
### flatten
![скриншот задания](images/lab02/arrays/flatten/arrays_flatten1.png)

![скриншот задания](images/lab02/arrays/flatten/arrays_flatten2.png)

![скриншот задания](images/lab02/arrays/flatten/arrays_flatten3.png)

![скриншот задания](images/lab02/arrays/flatten/arrays_flatten4.png)
### min_max
![скриншот задания](images/lab02/arrays/min_max/arrays_min_max1.png)

![скриншот задания](images/lab02/arrays/min_max/arrays_min_max2.png)

![скриншот задания](images/lab02/arrays/min_max/arrays_min_max3.png)

![скриншот задания](images/lab02/arrays/min_max/arrays_min_max4.png)

![скриншот задания](images/lab02/arrays/min_max/arrays_min_max5.png)
### unique_sorted
![скриншот задания](images/lab02/arrays/unique_sorted/arrays_unique_sorted1.png)

![скриншот задания](images/lab02/arrays/unique_sorted/arrays_unique_sorted2.png)

![скриншот задания](images/lab02/arrays/unique_sorted/arrays_unique_sorted3.png)

![скриншот задания](images/lab02/arrays/unique_sorted/arrays_unique_sorted4.png)
## Задание 2 - Matrix
    m=[[1, 2], [3]]
    
    def transpose(mat: list[list[float | int]]) -> list[list]:
        if not m:
            return m
        for i in range (len(m)):
            if len(m[i]) != len(m[0]):
                raise ValueError("Матрица рваная")
        transposed = list(map(list, zip(*m)))
        return transposed
    
    
    def row_sums(mat: list[list[float | int]]) -> list[float]:
        for i in range (len(m)):
            if len(m[i]) != len(m[0]):
                raise ValueError("Матрица рваная")
        rowsums = [sum(row) for row in m]
        return rowsums
    
    
    def col_sums(mat: list[list[float | int]]) -> list[float]:
        for i in range (len(m)):
            if len(m[i]) != len(m[0]):
                raise ValueError("Матрица рваная")
        colsums = []
        for j in range(len(m[0])):  
            col_sum = 0
            for i in range(len(m)):  
                col_sum += m[i][j]
            colsums.append(col_sum)
        return colsums
                
    try:
        print(transpose(m))
    except ValueError as e:
        print(f"Ошибка: {e}") #transpose output
    
    try:
        print(row_sums(m))
    except ValueError as a:
        print(f"Ошибка: {a}") #row_sums output
    
    try:
        print(col_sums(m))
    except ValueError as b:
        print(f"Ошибка: {b}") #col_sums output
### transpose
![скриншот задания](images/lab02/matrix/transpose/matrix_transpose1.png)

![скриншот задания](images/lab02/matrix/transpose/matrix_transpose2.png)

![скриншот задания](images/lab02/matrix/transpose/matrix_transpose3.png)

![скриншот задания](images/lab02/matrix/transpose/matrix_transpose4.png)

![скриншот задания](images/lab02/matrix/transpose/matrix_transpose5.png)
### row_sums
![скриншот задания](images/lab02/matrix/row_sums/matrix_row_sums1.png)

![скриншот задания](images/lab02/matrix/row_sums/matrix_row_sums2.png)

![скриншот задания](images/lab02/matrix/row_sums/matrix_row_sums3.png)

![скриншот задания](images/lab02/matrix/row_sums/matrix_row_sums4.png)
### col_sums
![скриншот задания](images/lab02/matrix/col_sums/matrix_col_sums1.png)

![скриншот задания](images/lab02/matrix/col_sums/matrix_col_sums2.png)

![скриншот задания](images/lab02/matrix/col_sums/matrix_col_sums3.png)

![скриншот задания](images/lab02/matrix/col_sums/matrix_col_sums4.png)
## Задание 3 - Tuples
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
    ![скриншот задания](images/lab02/tuples/tuples.png)
# Лабораторная работа 3
## Задание A
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
![скриншот задания](images/lab03/text/text.png)
![скриншот задания](images/lab03/text/text2.png)
## Задание В
    #!/usr/bin/env python3
    import sys
    import os
    sys.path.insert(0, os.path.dirname(__file__))
    from lib.text import normalize, tokenize, count_freq, top_n
    
    text = sys.stdin.read().strip()
    if not text: 
        print("No input")
        sys.exit()
    
    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)
    top_words = top_n(freq, 5)
    
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}:{count}")
![скриншот задания](images/lab03/text_stats/text_stats1.png)
![скриншот задания](images/lab03/text_stats/text_stats2.png)
![скриншот задания](images/lab03/text_stats/text_stats3.png)
![скриншот задания](images/lab03/text_stats/text_stats4.png)
![скриншот задания](images/lab03/text_stats/text_stats5.png)
