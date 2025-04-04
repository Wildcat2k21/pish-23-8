# Проект: Управление Очередью и Банковскими Вкладами

## Описание
Данный проект включает в себя две основные части:
1. **Управление банковскими вкладами** - предоставляет различные типы вкладов и механизм их подбора.
2. **Очередь (Queue)** - реализует структуру данных "очередь" с возможностью сохранения и загрузки данных.

## Структура проекта
- `main.py` - основной скрипт, который демонстрирует работу очереди.
- `task1_bank.py` - модуль управления банковскими вкладами, включает классы:
  - `BankDeposit` - базовый класс банковского вклада.
  - `TermDeposit` - вклад с простыми процентами.
  - `BonusDeposit` - вклад с бонусной системой.
  - `CapDeposit` - вклад с капитализацией процентов.
  - `DepositAdvisor` - система подбора лучшего вклада.
- `task2_queue.py` - реализация структуры данных "очередь" с методами:
  - `enqueue(item)` - добавляет элемент в очередь.
  - `dequeue()` - удаляет и возвращает первый элемент.
  - `peek()` - возвращает первый элемент без удаления.
  - `save(filename)` - сохраняет очередь в файл.
  - `load(filename)` - загружает очередь из файла.
  - `from_string(string)` - создаёт очередь из строки.

## Установка и запуск
1. Убедитесь, что установлен Python 3.6+.
2. Склонируйте репозиторий и перейдите в директорию проекта:
   ```sh
   git clone <URL_репозитория>
   cd <папка_проекта>
   ```
3. Запустите тестирование очереди:
   ```sh
   python main.py
   ```
4. Для работы с банковскими вкладами запустите:
   ```sh
   python task1_bank.py
   ```

## Пример использования
Пример работы с очередью:
```python
from task2_queue import Queue
q = Queue(max_size=3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # 1
print(q.peek())  # 2
```

Пример подбора вклада:
```python
from task1_bank import DepositAdvisor
advisor = DepositAdvisor()
result = advisor.find_best_deposit(50000, "RUB", 12)
if result:
    deposit, profit = result
    print(f"Лучший вклад: {deposit.name}, прибыль: {profit} RUB")
```

## Лицензия
Этот проект распространяется под MIT License.
