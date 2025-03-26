from task2_queue import Queue

def test_queue():
    # Создание очереди
    q = Queue(max_size=5)
    print(f"Создана очередь: {q}")
    print(f"Пуста ли очередь? {q.is_empty}")
    
    # Добавление элементов
    for i in range(1, 6):
        q.enqueue(i)
        print(f"Добавлен {i}, очередь: {q}")
    
    try:
        q.enqueue(6)
    except OverflowError as e:
        print(f"Ошибка: {e}")
    
    # Просмотр и извлечение элементов
    print(f"Первый элемент: {q.peek()}")
    print(f"Извлечен: {q.dequeue()}, очередь: {q}")
    
    # Проверка содержимого
    print(f"Содержит 3? {3 in q}")
    print(f"Размер очереди: {len(q)}")
    
    # Создание очереди из строки
    q2 = Queue.from_string("a, b, c")
    print(f"Очередь из строки: {q2}")
    
    # Сохранение и загрузка
    q2.save("queue.json")
    q3 = Queue.load("queue.json")
    print(f"Загруженная очередь: {q3}")
    
    # Объединение очередей
    combined = q + q3
    print(f"Объединенная очередь: {combined}")

if __name__ == "__main__":
    test_queue()