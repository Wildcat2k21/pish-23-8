from task2_hierarchy import WaterVehicle, WheeledVehicle, Car

if __name__ == "__main__":
    # Создаем экземпляры транспортных средств
    boat = WaterVehicle("Морской волк", 50, 2.5)
    bike = WheeledVehicle("Горный велосипед", 30, 2)
    car = Car("Седан", 180, "Toyota")
    
    # Демонстрация работы методов
    vehicles = [boat, bike, car]
    
    for vehicle in vehicles:
        vehicle.move()
        if isinstance(vehicle, Car):
            vehicle.honk()
        vehicle.stop()
        print(f"Текущая скорость: {vehicle.speed}\n")