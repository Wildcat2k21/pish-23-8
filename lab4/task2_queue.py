import json
from typing import Any, Optional

class Queue:
    """ Класс для реализации очереди с ограниченным размером """

    def __init__(self, max_size: Optional[int] = None):
        """ Инициализирует объект очереди с возможностью задания максимального размера """
        self._items = []
        self._max_size = max_size

    @property
    def size(self) -> int:
        """ Возвращает количество элементов в очереди """
        return len(self._items)

    @property
    def is_empty(self) -> bool:
        """ Проверяет, пуста ли очередь """
        return self.size == 0

    @property
    def is_full(self) -> bool:
        """ Проверяет, заполнена ли очередь до максимального размера """
        return self._max_size is not None and self.size >= self._max_size

    def enqueue(self, item: Any) -> None:
        """ Добавляет элемент в очередь, если она не полна """
        if self.is_full:
            raise OverflowError("Queue is full")
        self._items.append(item)

    def dequeue(self) -> Any:
        """ Удаляет и возвращает первый элемент из очереди """
        if self.is_empty:
            raise IndexError("Queue is empty")
        return self._items.pop(0)

    def peek(self) -> Any:
        """ Возвращает первый элемент очереди без его удаления """
        if self.is_empty:
            raise IndexError("Queue is empty")
        return self._items[0]

    def clear(self) -> None:
        """ Очищает очередь от всех элементов """
        self._items.clear()

    def __str__(self) -> str:
        """ Возвращает строковое представление очереди """
        return f"Queue({self._items})"

    def __repr__(self) -> str:
        """ Возвращает строковое представление очереди с максимальным размером """
        return f"Queue(max_size={self._max_size}, items={self._items})"

    def __len__(self) -> int:
        """ Возвращает количество элементов в очереди """
        return self.size

    def __contains__(self, item: Any) -> bool:
        """ Проверяет, содержится ли элемент в очереди """
        return item in self._items

    def __add__(self, other: 'Queue') -> 'Queue':
        """ Объединяет две очереди в одну """
        new_queue = Queue(max_size=self._max_size)
        new_queue._items = self._items + other._items
        return new_queue

    def __eq__(self, other: object) -> bool:
        """ Сравнивает две очереди на равенство """
        if not isinstance(other, Queue):
            return False
        return self._items == other._items

    @classmethod
    def from_string(cls, string: str) -> 'Queue':
        """ Создает очередь из строки, элементы разделены запятой """
        queue = cls()
        if string:
            items = [item.strip() for item in string.split(',')]
            for item in items:
                queue.enqueue(item)
        return queue

    def save(self, filename: str) -> None:
        """ Сохраняет очередь в файл в формате JSON """
        data = {
            'max_size': self._max_size,
            'items': self._items
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    @classmethod
    def load(cls, filename: str) -> 'Queue':
        """ Загружает очередь из файла в формате JSON """
        with open(filename, 'r') as f:
            data = json.load(f)
        queue = cls(max_size=data['max_size'])
        queue._items = data['items']
        return queue
