class Parrot:
    def __init__(self, name):
        self.name = name
        
    def say(self, len):
        print(self.name*len)

    def update(self, name):
        self.name = name

p1 = Parrot("Гав!")
p1.say(1)
p1.update("Мяу!")
p1.say(3)