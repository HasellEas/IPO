class Animal:
    def __init__(self, name):
        self.name = name
        print("Родилось животное "+self.name)
    def eat(self):
        print("Ням-ням")
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def makeNoise(self):
        print(self.name+" говорит Гррр")

create_animal = Animal("Блюцифер")
print(create_animal.getName())
create_animal.setName("Польнареф")
create_animal.eat()
create_animal.makeNoise()