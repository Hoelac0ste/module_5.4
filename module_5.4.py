class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        if args:
            name = args[0]
        cls.houses_history.append(name)
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__ (self):
        return (f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")

    def __del__(self):
        if self.name in House.houses_history:
            print(f'{self.name} снесён, но он останется в истории')
            House.houses_history.remove(self.name)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House("Отдохни", 5)
print(House.houses_history)
del h1
print(House.houses_history)
