class Roman:
    """Класс для работы с римскими числами, поддерживающий конвертацию и арифметические операции."""
    
    _roman_numerals = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
        'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
        'C': 100, 'CD': 400, 'D': 500, 'CM': 900,
        'M': 1000
    }
    _int_to_roman = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    def __init__(x, value):
        """Конструктор класса. Принимает либо строку с римским числом, либо целое число."""
        if isinstance(value, str):
            x.value = x.toArabic(value)
        elif isinstance(value, int):
            if value <= 0:
                raise ValueError("Roman numbers must be positive")
            x.value = value
        else:
            raise TypeError("Unsupported type")

    @staticmethod
    def toArabic(romanStr):
        """Преобразует римское число в арабское."""
        result = 0
        i = 0
        romanStr = romanStr.upper()
        while i < len(romanStr):
            if i + 1 < len(romanStr) and romanStr[i:i+2] in Roman._roman_numerals:
                result += Roman._roman_numerals[romanStr[i:i+2]]
                i += 2
            else:
                result += Roman._roman_numerals[romanStr[i]]
                i += 1
        return result

    @staticmethod
    def toRoman(arabicNum):
        """Преобразует арабское число в римское."""
        if arabicNum <= 0:
            raise ValueError("Roman numbers must be positive")
        roman_num = []
        for num, symbol in Roman._int_to_roman:
            while arabicNum >= num:
                roman_num.append(symbol)
                arabicNum -= num
        return ''.join(roman_num)

    def __add__(x, y):
        """Оператор сложения римских чисел."""
        if isinstance(y, Roman):
            return Roman(x.value + y.value)
        elif isinstance(y, int):
            return Roman(x.value + y)
        else:
            raise TypeError("Can only add Roman or int")

    def __sub__(x, y):
        """Оператор вычитания римских чисел."""
        if isinstance(y, Roman):
            result = x.value - y.value
        elif isinstance(y, int):
            result = x.value - y
        else:
            raise TypeError("Can only subtract Roman or int")
        if result <= 0:
            raise ValueError("Result must be positive")
        return Roman(result)

    def __mul__(x, y):
        """Оператор умножения римских чисел."""
        if isinstance(y, Roman):
            return Roman(x.value * y.value)
        elif isinstance(y, int):
            return Roman(x.value * y)
        else:
            raise TypeError("Can only multiply by Roman or int")

    def __truediv__(x, y):
        """Оператор целочисленного деления римских чисел."""
        if isinstance(y, Roman):
            result = x.value // y.value
        elif isinstance(y, int):
            result = x.value // y
        else:
            raise TypeError("Can only divide by Roman or int")
        if result <= 0:
            raise ValueError("Result must be positive")
        return Roman(result)

    def __str__(x):
        """Возвращает строковое представление римского числа."""
        return x.toRoman(x.value)

# Создание объектов
a = Roman("XIV")
b = Roman(5)

# Арифметические операции
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Альтернативные конструкторы
c = Roman.toRoman(42)
d = Roman.toArabic("XX")

print(c)
print(d)
