class NewCar:
    def __init__(self, speed, color, name_model, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name_model
        self.is_police = is_police

    def go(self):
        print(self.name + ' - машина поехала')

    def stop(self):
        print(self.name + ' - машина остановилась')

    def turn(self, direction):
        print(self.name + ' - машина повернула ' + direction)

class TownCar(NewCar):
    def __init__(self, speed, color, name_model, is_police = False):
        NewCar.__init__(self, speed, color, name_model, is_police = False)


class SportCar(NewCar):
    def __init__(self, speed, color, name_model, is_police=False):
        NewCar.__init__(self, speed, color, name_model, is_police=False)


class WorkCar(NewCar):
    def __init__(self, speed, color, name_model, is_police=False):
        NewCar.__init__(self, speed, color, name_model, is_police=False)

class PoliceCar(NewCar):
    def __init__(self, speed, color, name_model, is_police=False):
        NewCar.__init__(self, speed, color, name_model, is_police=True)


car1 = TownCar(25, 'red', 'Mitsubishi Outlender 550')
print(car1.go())
print(car1.stop())
print(car1.turn('налево'))

car2 = SportCar(77, 'blue', 'Mercedes-Benz')
print(car2.go())

car3 = WorkCar(88, 'blue', 'Mazda CX6')
print(car3.go())

car4 = PoliceCar(77, 'black', 'Ford Focus')
print(car4.go())
print(car4.stop())
print(car4.turn('направо'))
