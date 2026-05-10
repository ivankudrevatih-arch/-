from os import name





class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print(f'Hi, my name is {self.name}. I am {self.age} years old.')

    def birthday(self):
        self.age += 1
        print(f'The person{self.name} turned{self.age} years old ')


class Student(Human):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.grades = grades

def say.hi(self):



class Auto:


john = Student('John', 25, grades:[10,12,9,11,8,9])





bob = Human("bob", 30)
anna = Human("anna", 20)



for _ in range(5):
    bob.birthday()



bob.say_hi()
anna.say_hi()




















