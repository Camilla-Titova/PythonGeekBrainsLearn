# Задание 1
print('Задание 1')
from time import sleep


class TrafficLight:
    __color = ['Красный', 'Жёлтый', 'Зелёный']

    def running(self):
        color_switch = 0
        while color_switch < 3:
            print(f'Сфетфор переключается\n'f'{TrafficLight.__color[color_switch]}')
            if color_switch == 0:
                sleep(7)
            elif color_switch == 1:
                sleep(5)
            elif color_switch == 2:
                sleep(3)
            color_switch += 1


TrafficLight = TrafficLight()
TrafficLight.running()
# Задание 2
print('Задание 2')


class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width


class MassCount(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume


asphalt_mass = MassCount(20, 5000, 75)
print(asphalt_mass.mass())
# Задание 3
print('Задание 3')


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


person = Position('Ivan', 'Ivanov', 'Man', 70000, 30000)
print(person.get_full_name())
print(person.position)
print(person.get_total_income())
# Задание 4
print('Задание 4')


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


audi = SportCar(100, 'Red', 'Audi', False)
miniCooper = TownCar(30, 'White', 'miniCooper', False)
bmw = WorkCar(70, 'Rose', 'bmw', True)
ford = PoliceCar(110, 'Blue', 'Ford', True)
print(bmw.turn_left())
print(f'When {miniCooper.turn_right()}, then {audi.stop()}')
print(f'{bmw.go()} with speed exactly {bmw.show_speed()}')
print(f'{bmw.name} is {bmw.color}')
print(f'Is {audi.name} a police car? {audi.is_police}')
print(f'Is {bmw.name}  a police car? {bmw.is_police}')
print(audi.show_speed())
print(miniCooper.show_speed())
print(ford.police())
print(ford.show_speed())
# Задание 5
print('Задание 5')


class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки ручкой'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки карандашом'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки маркером'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
