class Themes:
    """Класс для управления списком тем."""
    
    def __init__(self, themes_list):
        """Инициализирует объект с начальным списком тем."""
        self.themes = list(themes_list)

    def add_theme(self, value):
        """Добавляет новую тему в конец списка."""
        self.themes.append(value)

    def shift_one(self):
        """Сдвигает темы на одну позицию вправо (последняя становится первой)."""
        if self.themes:  # Проверка, что список не пустой
            last_theme = self.themes.pop()  # Удаляем последний элемент
            self.themes.insert(0, last_theme)  # Вставляем его в начало

    def reverse_order(self):
        """Меняет порядок тем на обратный."""
        self.themes.reverse()

    def get_themes(self):
        """Возвращает текущий список тем в виде кортежа."""
        return tuple(self.themes)

    def get_first(self):
        """Возвращает первую тему в списке или None, если список пуст."""
        if self.themes:
            return self.themes[0]
        return None

print("Вариант 8")
# Пример 1
# Создаем экземпляр с темами 'weather' и 'rain'
t1 = Themes(['weather', 'rain'])  
t1.add_theme('warm')  # Добавляем тему 'warm'
print(t1.get_themes())  # ('weather', 'rain', 'warm')
t1.shift_one()  # Сдвигаем темы на одну вправо
print(t1.get_first())  # 'warm' (теперь первая тема)

# Пример 2
# Создаем экземпляр с темами 'sun' и 'feeding'
t1 = Themes(['sun', 'feeding'])
t1.add_theme('cool')  # Добавляем тему 'cool'
t1.shift_one()  # Сдвигаем темы на одну вправо
print(t1.get_first())  # 'cool' (теперь первая тема)
t1.reverse_order()  # Меняем порядок тем на обратный
print(t1.get_themes())  # ('feeding', 'sun', 'cool')
