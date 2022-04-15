import time

class Creature():
    def getName(self):
        return self.name
class Animal(Creature):
    def sleep(self, times):
        print("Сон на "+str(times)+" секунд")
        time.sleep(times)
class Pet(Creature):
    def play(self):
        print("Игра с питомем")
class Dog(Animal, Pet, Creature):
    def __init__(self, name):
        self.name = name
        print("Родился пёс "+self.name)

entity = Dog("Рузвельт")
entity.play()
entity.sleep(1)
print(entity.getName())