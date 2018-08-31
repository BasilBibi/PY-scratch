from abc import *


class Animal(ABC):

    def __init__(self, n):
        self.name = n

    def whats_your_name(self):
        print(f'my name is {self.name}')

    @abstractmethod
    def move(self):
        return


class Cat(Animal):
    def move(self):
        print('move like a cat')


class Dog(Animal):
    def move(self):
        print('move like a dog')


class Flea(Animal):
    def move(self):
        print('move like a flea')

    def whats_your_name(self):
        print('Fuck you I am Flea!')


animal = Cat(n='Lulu')
animal.move()
animal.whats_your_name()

animal = Dog(n='Spooky')
animal.move()
animal.whats_your_name()

animal = Flea(n='Nigel')
animal.move()
animal.whats_your_name()