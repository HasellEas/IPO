class Parrot:
    def __init__(self, name):
        self.name = name
        
    def say(self):
        print(self.name)

    def update(self, name):
        self.name = name

p1 = Parrot("Гав!")
p1.say()
p1.update("Мяу!")
p1.say()