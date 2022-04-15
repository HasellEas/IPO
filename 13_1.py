class Unit:
    def __init__(self, index, hp):
        self.hp = hp
        self.mhp = hp
        self.index = str(index)
        self.mp = 100
    def hit(self):
        print("Игроку "+str(self.index)+" нанесён урон 20 единиц. Мана отрегенировала на 30 единиц!")
        self.hp -= 20
        self.mp += 30
    def get(self):
        return self.hp
    def getm(self):
        return self.mp
    def magic_spell(self):
        if self.mp >= 100:
            print("Враг использовал магию! Игроку "+self.index+" наноситься урон 50 единиц!")
            self.hp -= 50
        else:
            print("Враг хотел использовать магию, но ему не хватило маны!")
    def heal(self):
        if self.hp >= self.mhp: 
            print("Здоровье "+self.index+" игрока максимально!")
        else:
            if self.mp <= 50:
                print("Игрок "+self.index+" собирался использовать исцеление, но не хватило маны!")
            else:
                self.mp -= 50
                self.hp += 60
                print("Игрок "+self.index+" использует заклинание лечения! Его здоровье увеличино на 60 единиц!")

Guard1 = Unit(1, 100)
Guard2 = Unit(2, 100)

import random

while Guard2.get() >= 0 and Guard1.get() >= 0:
    if random.randint(0,1) == 1:
        x = random.randint(0,2)
        if x == 0:
            Guard1.hit()
        elif x == 1:
            Guard2.heal()
        elif x == 2:
            Guard1.magic_spell()
    else:
        x = random.randint(0,2)
        if x == 0:
            Guard2.hit()
        elif x == 1:
            Guard1.heal()
        elif x == 2:
            Guard2.magic_spell()
    print("Здоровье игрока 1: "+str(Guard1.get())+" MP: "+str(Guard1.getm())+"\nЗдоровье игрока 2: "+str(Guard2.get())+" MP: "+str(Guard2.getm()))

if Guard2.get() <= 0:
    print("Игрок 1 ПОБЕДИЛ!!!")
else:
    print("Игрок 2 ПОБЕДИЛ!!!")