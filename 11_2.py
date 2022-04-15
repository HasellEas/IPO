class Parrot:
    def __init__(self, name):
        self.name = name
        
    def say(self):
        print(self.name)

p1 = Parrot("Гав!")
p2 = Parrot("Мяу!")
p1.say()
p2.say()