from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Абстрактный базовый класс для всех транспортных средств"""
    
    def __init__(self, name: str, max_speed: float):
        self._name = name        # защищенное поле - название ТС
        self._max_speed = max_speed  # защищенное поле - макс. скорость
        self._current_speed = 0  # защищенное поле - текущая скорость
    
    @abstractmethod
    def move(self) -> None:
        """Абстрактный метод для движения транспортного средства"""
        pass
    
    def stop(self) -> None:
        """Остановка транспортного средства"""
        self._current_speed = 0
        print(f"{self._name} остановился")
    
    @property
    def speed(self) -> float:
        """Текущая скорость транспортного средства"""
        return self._current_speed

class WaterVehicle(Vehicle):
    """Класс для водных транспортных средств"""
    
    def __init__(self, name: str, max_speed: float, draft: float):
        super().__init__(name, max_speed)
        self.__draft = draft  # приватное поле - осадка судна
    
    def move(self) -> None:
        """Реализация движения для водного транспорта"""
        self._current_speed = self._max_speed * 0.8  # вода медленнее
        print(f"{self._name} плывет со скоростью {self._current_speed} узлов")

class WheeledVehicle(Vehicle):
    """Класс для колесных транспортных средств"""
    
    def __init__(self, name: str, max_speed: float, wheel_count: int):
        super().__init__(name, max_speed)
        self.__wheel_count = wheel_count  # приватное поле - кол-во колес
    
    def move(self) -> None:
        """Реализация движения для колесного транспорта"""
        self._current_speed = self._max_speed
        print(f"{self._name} едет со скоростью {self._current_speed} км/ч")

class Car(WheeledVehicle):
    """Класс для автомобилей (наследуется от колесных ТС)"""
    
    def __init__(self, name: str, max_speed: float, brand: str):
        super().__init__(name, max_speed, 4)  # у автомобиля всегда 4 колеса
        self.__brand = brand  # приватное поле - марка автомобиля
    
    def move(self) -> None:
        """Реализация движения для автомобиля"""
        self._current_speed = self._max_speed * 0.9  # учитываем пробки
        print(f"Автомобиль {self.__brand} {self._name} движется со скоростью {self._current_speed} км/ч")
    
    def honk(self) -> None:
        """Дополнительный метод - сигналить"""
        print(f"{self.__brand} сигналит: Бип-бип!")