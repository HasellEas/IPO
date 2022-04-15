class Cat:
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color

    def meow(self):
        print("мяуканье "+self.color+" "+self.name+" "+str(self.weight)+" kg")

kitty = Cat("Пуся", 7, "Серый")
kitty.meow()