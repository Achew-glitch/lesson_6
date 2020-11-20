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

a = (Stationery('stationey'), Pen('Pen'), Pencil('Pencil'), Handle('Handle'))

for el in a:
    el.draw()