from typing import Any, Iterator, Optional


class Node:
    """Узел односвязного списка."""
    
    def __init__(self, value: Any, next_node: Optional['Node'] = None) -> None:
        """
        Инициализация узла.
        
        Args:
            value: Значение узла
            next_node: Ссылка на следующий узел
        """
        self.value: Any = value
        self.next: Optional[Node] = next_node
    
    def __repr__(self) -> str:
        """Строковое представление узла."""
        return f"[{self.value}]"


class SinglyLinkedList:
    """Односвязный список."""
    
    def __init__(self) -> None:
        """Инициализация пустого списка."""
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0
    
    def append(self, value: Any) -> None:
        """
        Добавить элемент в конец списка.
        Сложность: O(1) с использованием tail.
        """
        new_node = Node(value)
        
        if self.is_empty():
            # Если список пуст, новый узел становится и головой и хвостом
            self.head = new_node
            self.tail = new_node
        else:
            # Добавляем в конец и обновляем tail
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, value: Any) -> None:
        """
        Добавить элемент в начало списка.
        Сложность: O(1).
        """
        new_node = Node(value, self.head)
        
        if self.is_empty():
            # Если список пуст, новый узел становится и головой и хвостом
            self.tail = new_node
        
        self.head = new_node
        self._size += 1
    
    def insert(self, idx: int, value: Any) -> None:
        """
        Вставить элемент по индексу.
        Сложность: O(n) в худшем случае.
        
        Args:
            idx: Индекс для вставки
            value: Значение для вставки
            
        Raises:
            IndexError: если индекс вне диапазона [0, len(list)]
        """
        if idx < 0 or idx > self._size:
            raise IndexError(f"Индекс {idx} вне диапазона [0, {self._size}]")
        
        if idx == 0:
            # Вставка в начало
            self.prepend(value)
        elif idx == self._size:
            # Вставка в конец
            self.append(value)
        else:
            # Вставка в середину
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            
            new_node = Node(value, current.next)
            current.next = new_node
            self._size += 1
    
    def remove_at(self, idx: int) -> None:
        """
        Удалить элемент по индексу.
        Сложность: O(n) в худшем случае.
        
        Args:
            idx: Индекс элемента для удаления
            
        Raises:
            IndexError: если индекс вне диапазона или список пуст
        """
        if self.is_empty():
            raise IndexError("Попытка удаления из пустого списка")
        
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Индекс {idx} вне диапазона [0, {self._size - 1}]")
        
        if idx == 0:
            # Удаление первого элемента
            self.head = self.head.next
            if self.head is None:
                # Если список стал пустым, обновляем tail
                self.tail = None
        else:
            # Удаление из середины или конца
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            
            # current теперь указывает на элемент перед удаляемым
            current.next = current.next.next
            
            # Если удалили последний элемент, обновляем tail
            if current.next is None:
                self.tail = current
        
        self._size -= 1
    
    def remove(self, value: Any) -> bool:
        """
        Удалить первое вхождение значения.
        Сложность: O(n).
        
        Args:
            value: Значение для удаления
            
        Returns:
            True если элемент был удален, иначе False
        """
        if self.is_empty():
            return False
        
        # Специальный случай: удаление головы
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return True
        
        # Поиск элемента для удаления
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next
        
        # Если нашли элемент
        if current.next is not None:
            current.next = current.next.next
            
            # Если удалили последний элемент, обновляем tail
            if current.next is None:
                self.tail = current
            
            self._size -= 1
            return True
        
        return False
    
    def is_empty(self) -> bool:
        """Проверить, пуст ли список. Сложность: O(1)."""
        return self.head is None
    
    def __iter__(self) -> Iterator[Any]:
        """
        Итератор по значениям списка.
        Сложность итерации по всему списку: O(n).
        """
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
    
    def __len__(self) -> int:
        """Вернуть количество элементов. Сложность: O(1)."""
        return self._size
    
    def __repr__(self) -> str:
        """Строковое представление списка в виде [A] -> [B] -> None."""
        if self.is_empty():
            return "SinglyLinkedList([])"
        
        result = []
        current = self.head
        while current is not None:
            result.append(str(current))
            current = current.next
        
        return " -> ".join(result) + " -> None"
    
    def to_list(self) -> list:
        """Преобразовать список в обычный Python list. Сложность: O(n)."""
        return list(self)