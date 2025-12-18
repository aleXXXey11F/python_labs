import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.lab10.structures import Stack, Queue
from src.lab10.linked_list import SinglyLinkedList


def demonstrate_stack():
    """Демонстрация работы стека."""
    print("=" * 50)
    print("Демонстрация стека (Stack):")
    print("=" * 50)
    
    stack = Stack()
    print(f"Создан пустой стек: {stack}")
    print(f"Стек пуст? {stack.is_empty()}")
    
    # Добавляем элементы
    for i in range(1, 6):
        stack.push(f"Элемент {i}")
        print(f"push('Элемент {i}') -> {stack}")
    
    print(f"\nВерхний элемент (peek): {stack.peek()}")
    print(f"Длина стека: {len(stack)}")
    
    # Извлекаем элементы
    print("\nИзвлечение элементов:")
    while not stack.is_empty():
        print(f"pop() -> {stack.pop()}, стек: {stack}")
    
    print(f"\nСтек пуст? {stack.is_empty()}")


def demonstrate_queue():
    """Демонстрация работы очереди."""
    print("\n" + "=" * 50)
    print("Демонстрация очереди (Queue):")
    print("=" * 50)
    
    queue = Queue()
    print(f"Создана пустая очередь: {queue}")
    print(f"Очередь пуста? {queue.is_empty()}")
    
    # Добавляем элементы
    for i in range(1, 6):
        queue.enqueue(f"Задача {i}")
        print(f"enqueue('Задача {i}') -> {queue}")
    
    print(f"\nПервый элемент (peek): {queue.peek()}")
    print(f"Длина очереди: {len(queue)}")
    
    # Извлекаем элементы
    print("\nИзвлечение элементов:")
    while not queue.is_empty():
        print(f"dequeue() -> {queue.dequeue()}, очередь: {queue}")
    
    print(f"\nОчередь пуста? {queue.is_empty()}")


def demonstrate_linked_list():
    """Демонстрация работы односвязного списка."""
    print("\n" + "=" * 50)
    print("Демонстрация односвязного списка (SinglyLinkedList):")
    print("=" * 50)
    
    lst = SinglyLinkedList()
    print(f"Создан пустой список: {lst}")
    print(f"Список пуст? {lst.is_empty()}")
    
    # Добавляем элементы в конец
    print("\nДобавление в конец (append):")
    for i in range(1, 4):
        lst.append(i * 10)
        print(f"append({i * 10}) -> {lst}")
    
    # Добавляем элементы в начало
    print("\nДобавление в начало (prepend):")
    lst.prepend(5)
    print(f"prepend(5) -> {lst}")
    lst.prepend(1)
    print(f"prepend(1) -> {lst}")
    
    # Вставка по индексу
    print("\nВставка по индексу (insert):")
    lst.insert(2, 15)
    print(f"insert(2, 15) -> {lst}")
    lst.insert(0, 0)
    print(f"insert(0, 0) -> {lst}")
    lst.insert(len(lst), 40)
    print(f"insert({len(lst)-1}, 40) -> {lst}")
    
    # Итерация по списку
    print(f"\nИтерация по списку:")
    print(f"Список как Python list: {lst.to_list()}")
    
    # Удаление по индексу
    print("\nУдаление по индексу (remove_at):")
    lst.remove_at(2)
    print(f"remove_at(2) -> {lst}")
    lst.remove_at(0)
    print(f"remove_at(0) -> {lst}")
    
    # Удаление по значению
    print("\nУдаление по значению (remove):")
    print(f"remove(30): {lst.remove(30)} -> {lst}")
    print(f"remove(99) (не существует): {lst.remove(99)} -> {lst}")
    
    print(f"\nИтоговый список: {lst}")
    print(f"Длина списка: {len(lst)}")
    print(f"Список как Python list: {lst.to_list()}")


def benchmark_comparison():
    """Сравнение производительности структур данных."""
    print("\n" + "=" * 50)
    print("Сравнение производительности:")
    print("=" * 50)
    
    import time
    import random
    
    test_size = 10000
    
    # Тестирование Stack
    print(f"\nТестирование Stack ({test_size} операций):")
    stack = Stack()
    start = time.time()
    
    for i in range(test_size):
        stack.push(i)
    
    for _ in range(test_size):
        stack.pop()
    
    stack_time = time.time() - start
    print(f"Время выполнения: {stack_time:.6f} секунд")
    
    # Тестирование Queue
    print(f"\nТестирование Queue ({test_size} операций):")
    queue = Queue()
    start = time.time()
    
    for i in range(test_size):
        queue.enqueue(i)
    
    for _ in range(test_size):
        queue.dequeue()
    
    queue_time = time.time() - start
    print(f"Время выполнения: {queue_time:.6f} секунд")
    
    # Тестирование SinglyLinkedList
    print(f"\nТестирование SinglyLinkedList ({test_size} операций):")
    lst = SinglyLinkedList()
    start = time.time()
    
    for i in range(test_size):
        lst.append(i)
    
    # Обратите внимание: удаление из начала связного списка медленное!
    for _ in range(test_size):
        lst.remove_at(0)
    
    linked_list_time = time.time() - start
    print(f"Время выполнения: {linked_list_time:.6f} секунд")
    
    # Вывод сравнения
    print(f"\n" + "=" * 50)
    print("Результаты сравнения:")
    print(f"Stack:    {stack_time:.6f} секунд")
    print(f"Queue:    {queue_time:.6f} секунд")
    print(f"LinkedList: {linked_list_time:.6f} секунд")
    print(f"\nLinkedList медленнее Stack в {linked_list_time/stack_time:.1f} раз")
    print(f"LinkedList медленнее Queue в {linked_list_time/queue_time:.1f} раз")


if __name__ == "__main__":
    demonstrate_stack()
    demonstrate_queue()
    demonstrate_linked_list()
    benchmark_comparison()