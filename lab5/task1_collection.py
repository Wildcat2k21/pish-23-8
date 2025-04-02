import json
from typing import Any, Optional, List, Union

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

class QueueCollection:
    """Класс-контейнер для хранения коллекции объектов Queue"""
    
    def __init__(self, queues: List['Queue'] = None):
        """Инициализация контейнера"""
        self._node_data = queues if queues is not None else []
    
    def __str__(self) -> str:
        """Строковое представление коллекции"""
        return f"QueueCollection with {len(self._node_data)} queues"
    
    def __getitem__(self, index: Union[int, slice]) -> Union['Queue', 'QueueCollection']:
        """Поддержка индексации и срезов"""
        if isinstance(index, slice):
            return QueueCollection(self._node_data[index])
        return self._node_data[index]
    
    def add(self, value: 'Queue') -> None:
        """Добавление очереди в коллекцию"""
        if not isinstance(value, Queue):
            raise TypeError("Only Queue objects can be added")
        self._node_data.append(value)
    
    def remove(self, index: int) -> None:
        """Удаление очереди по индексу"""
        if not 0 <= index < len(self._node_data):
            raise IndexError("Index out of range")
        del self._node_data[index]
    
    def save(self, filename: str) -> None:
        """Сохранение коллекции в JSON-файл"""
        data = {
            'queues': [
                {
                    'max_size': queue._max_size,
                    'items': queue._items
                }
                for queue in self._node_data
            ]
        }
        with open(filename, 'w') as f:
            json.dump(data, f)
    
    @classmethod
    def load(cls, filename: str) -> 'QueueCollection':
        """Загрузка коллекции из JSON-файла"""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        queues = []
        for queue_data in data['queues']:
            queue = Queue(max_size=queue_data['max_size'])
            queue._items = queue_data['items']
            queues.append(queue)
        
        return cls(queues)
    
if __name__ == "__main__":
    # Создаем несколько очередей
    q1 = Queue(max_size=3)
    q1.enqueue(1)
    q1.enqueue(2)
    
    q2 = Queue(max_size=5)
    q2.enqueue('a')
    q2.enqueue('b')
    q2.enqueue('c')
    
    # 1. Создание коллекции
    collection = QueueCollection()
    print(f"Создана пустая коллекция: {collection}")
    
    # 2. Добавление элементов
    collection.add(q1)
    collection.add(q2)
    print(f"\nПосле добавления 2 очередей: {collection}")
    
    # 3. Проверка индексации
    print(f"\nПервая очередь: {collection[0]}")
    print(f"Срез из 1 элемента: {collection[1:2]}")
    
    # 4. Удаление элемента
    collection.remove(0)
    print(f"\nПосле удаления первой очереди: {collection}")
    
    # 5. Сохранение и загрузка
    collection.save("queues.json")
    loaded_collection = QueueCollection.load("queues.json")
    print(f"\nЗагруженная коллекция: {loaded_collection}")
    
    # 6. Проверка работы среза
    print(f"\nПервый элемент загруженной коллекции: {loaded_collection[0]}")