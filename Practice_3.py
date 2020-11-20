class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Имя сотрудника: {self.name}\nФамилия сотрудника: {self.surname}')

    def get_total_income(self):
        print(f'Суммарный доход сотрудника {self.name} {self.surname}: {sum(self._income.values())}')

a = Position('Artem', 'Kovzik', 'Backend Developer', 80000, 25000)
a.get_full_name()
a.get_total_income()
