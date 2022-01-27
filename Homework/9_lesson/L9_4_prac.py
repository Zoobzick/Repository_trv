class Car:
    speed: float
    _color: str
    _name: str
    _is_police: bool = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f"{self.name} is moving")

    def stop(self):
        print(f"{self.name} is stopped")

    def turn_direction(self, direction: str):
        print(f"{self.name} turned {direction}")

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        speed = super().show_speed()
        if speed > 60:
            print(f"You have exceeded the speed limit by {speed - 60} km/h")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        speed = super().show_speed()
        if speed > 40:
            print(f"You have exceeded the speed limit by {speed - 40} km/h")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self._is_police = True


car = Car(50, "Blue", "Lexus")
town_car = TownCar(140, "yellow", "BMW")
sport_car = SportCar(230, "Green", "Lamborghini")
work_car = WorkCar(90, "Red", "Toyota")
police_car = PoliceCar(90, "Black/White", "Chevrolet")

cars = [car, town_car, sport_car, work_car, police_car]

for car in cars:
    print(car.name)
    print(car.color)
    print(car._is_police)
    print(car.show_speed(), "\n")






