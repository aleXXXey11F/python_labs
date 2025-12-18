from collections import deque
from typing import Any


class Stack:
    """Реализация стека (LIFO) на базе списка."""
    
    def __init__(self) -> None:
        """Инициализация пустого стека."""
        self._data: list[Any] = []
    
    def push(self, item: Any) -> None:
        """Добавить элемент на вершину стека. Сложность: O(1)."""
        self._data.append(item)
    
    def pop(self) -> Any:
        """
        Удалить и вернуть верхний элемент стека.
        Сложность: O(1).
        
        Raises:
            IndexError: если стек пуст
        """
        if self.is_empty():
            raise IndexError("Попытка извлечения из пустого стека")
        return self._data.pop()
    
    def peek(self) -> Any | None:
        """
        Вернуть верхний элемент без удаления.
        Сложность: O(1).
        
        Returns:
            Верхний элемент или None, если стек пуст
        """
        if self.is_empty():
            return None
        return self._data[-1]
    
    def is_empty(self) -> bool:
        """Проверить, пуст ли стек. Сложность: O(1)."""
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """Вернуть количество элементов в стеке. Сложность: O(1)."""
        return len(self._data)
    
    def __repr__(self) -> str:
        """Строковое представление стека."""
        return f"Stack({self._data})"


class Queue:
    """Реализация очереди (FIFO) на базе deque."""
    
    def __init__(self) -> None:
        """Инициализация пустой очереди."""
        self._data: deque[Any] = deque()
    
    def enqueue(self, item: Any) -> None:
        """Добавить элемент в конец очереди. Сложность: O(1)."""
        self._data.append(item)
    
    def dequeue(self) -> Any:
        """
        Удалить и вернуть первый элемент очереди.
        Сложность: O(1).
        
        Raises:
            IndexError: если очередь пуста
        """
        if self.is_empty():
            raise IndexError("Попытка извлечения из пустой очереди")
        return self._data.popleft()
    
    def peek(self) -> Any | None:
        """
        Вернуть первый элемент без удаления.
        Сложность: O(1).
        
        Returns:
            Первый элемент или None, если очередь пуста
        """
        if self.is_empty():
            return None
        return self._data[0]
    
    def is_empty(self) -> bool:
        """Проверить, пуста ли очередь. Сложность: O(1)."""
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """Вернуть количество элементов в очереди. Сложность: O(1)."""
        return len(self._data)
    
    def __repr__(self) -> str:
        """Строковое представление очереди."""
        return f"Queue({list(self._data)})"