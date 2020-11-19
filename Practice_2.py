class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
    def mass(self, asph_mass, depth):
        return self._width * self._lenght * asph_mass * depth

lenght = int(input('Какой длинны будет дорога: '))
width = int(input('Какой ширины будет дорога: '))
a = Road(lenght, width)
print(f'Необходимая масса асфальта для укладки асфальта площадью {lenght * width} m2: {a.mass(25, 5) / 1000} т')