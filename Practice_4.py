class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f'{self.name} is running')

    def stop(self):
        print(f'{self.name} is stop')

    def turn(self, direction):
        print(f'{self.name} is turn {direction}')

    def show_speed(self):
        print(f'{self.name} is current speed: {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        print('This is Town Car')

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} speed is above 60!')

        else:
            print(f'{self.name} is current speed: {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        print('This is Sport Car')


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        print('This is Work Car')

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} speed is above 60!')

        else:
            print(f'{self.name} is current speed: {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True
        print('This is Police Car')


cars = [TownCar(80, 'Red', 'Jimmy'), \
        SportCar(240, 'Yellow', 'Ferrary'), \
        WorkCar(50, 'Green', 'Cat'), \
        PoliceCar(100, 'White', 'Ford')]

for el in cars:
    print(f'Color {el.name} is {el.color}')
    print(f'Does is {el.name} police car?\n{el.is_police}')
    el.go()
    el.stop()
    el.turn('right')
    el.show_speed()
