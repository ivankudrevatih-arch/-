class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print(f"Привіт, мене звати {self.name}. Мені {self.age} років.")

    def birthday(self):
        self.age += 1
        print(f"{self.name} святкує день народження! Тепер вік: {self.age}")


class Student(Human):
    def __init__(self, name, age, grades):
        # Викликаємо конструктор батьківського класу Human
        super().__init__(name, age)
        self.grades = grades

    def say_hi(self):
        # Використовуємо метод батька + додаємо своє
        super().say_hi()
        average = sum(self.grades) / len(self.grades) if self.grades else 0
        print(f"Я студент, мій середній бал: {average:.2f}. Мої оцінки: {self.grades}")


class Auto:
    def __init__(self):
        # Список, де ми будемо зберігати об'єкти пасажирів
        self.passengers = []

    def add_passenger(self, passenger):
        # Додаємо об'єкт (людину або студента) до списку
        self.passengers.append(passenger)
        print(f"{passenger.name} сів у машину.")

    def show_passengers(self):
        print("\n--- Список пасажирів у машині ---")
        if not self.passengers:
            print("Машина порожня.")
        else:
            for person in self.passengers:
                print(f"- {person.name} ({type(person).__name__})")
        print("---------------------------------\n")


# --- ПЕРЕВІРКА РОБОТИ ---

# 1. Створюємо об'єкти
john = Student(name="Джон", age=25, grades=[10, 12, 9, 11, 8, 9])
bob = Human(name="Боб", age=30)
anna = Human(name="Анна", age=20)

# 2. Перевіряємо методи класів
john.say_hi()
bob.birthday()

# 3. Працюємо з машиною
my_car = Auto()

my_car.add_passenger(john)
my_car.add_passenger(bob)
my_car.add_passenger(anna)

# 4. Виводимо всіх, хто в машині
my_car.show_passengers()