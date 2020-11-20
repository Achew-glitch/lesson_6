class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start drawing')

class Pen(Stationery):
    def draw(self):
        print(f'Start {self.title} drawing')

class Pencil(Stationery):
    def draw(self):
        print(f'Start {self.title} drawing')

class Handle(Stationery):
    def draw(self):
        print(f'Start {self.title} drawing')

a = Stationery('stationey')
b = Pen('Pen')
c = Pencil('Pencil')
d = Handle('Handle')

a.draw()
b.draw()
c.draw()
d.draw()