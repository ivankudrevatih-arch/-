class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print(f'Hi, my name is {self.name}. I am {self.age} years old.')

    def birthday(self):
        self.age += 1
        print(f'The person {self.name} turned {self.age} years old')


class Student(Human):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.grades = grades

    def say_hi(self):
        print(f'Привіт, я студент {self.name}! Мої оцінки: {self.grades}')


class Auto:
    def __init__(self):
        self.passengers = []

    def add_passenger(self, passenger):

        if passenger in self.passengers:
            print(f"Пасажир {passenger.name} вже в авто!")
            return

        self.passengers.append(passenger)
        print(f"{passenger.name} сів в авто")

    def print_all(self):
        print('----Всі пасажири авто----')

        for passenger in self.passengers:
            passenger.say_hi()

        print('-------------------------')


john = Student("John", 25, [10, 12, 9, 11])
bob = Human("Bob", 30)
anna = Human("Anna", 20)

car = Auto()

car.add_passenger(john)
car.add_passenger(john)
car.add_passenger(bob)
car.add_passenger(anna)

car.print_all()