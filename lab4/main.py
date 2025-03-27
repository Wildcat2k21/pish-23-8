from task2_queue import Queue

def test_queue():
    """Тестирование функциональности очереди"""
    # Создание очереди
    q = Queue(max_size=5)
    print(f"Создана очередь: {q}")
    print(f"Пуста ли очередь? {q.is_empty}")
    
    # Добавление элементов в очередь
    for i in range(1, 6):
        q.enqueue(i)
        print(f"Добавлен {i}, очередь: {q}")
    
    try:
        # Попытка добавить элемент в переполненную очередь
        q.enqueue(6)
    except OverflowError as e:
        print(f"Ошибка: {e}")
    
    # Просмотр первого элемента в очереди
    print(f"Первый элемент: {q.peek()}")
    
    # Извлечение элемента из очереди
    print(f"Извлечен: {q.dequeue()}, очередь: {q}")
    
    # Проверка содержимого очереди
    print(f"Содержит 3? {3 in q}")
    print(f"Размер очереди: {len(q)}")
    
    # Создание очереди из строки
    q2 = Queue.from_string("a, b, c")
    print(f"Очередь из строки: {q2}")
    
    # Сохранение состояния очереди в файл
    q2.save("queue.json")
    
    # Загрузка состояния очереди из файла
    q3 = Queue.load("queue.json")
    print(f"Загруженная очередь: {q3}")
    
    # Объединение двух очередей
    combined = q + q3
    print(f"Объединенная очередь: {combined}")

if __name__ == "__main__":
    # Запуск тестирования очереди
    test_queue()
