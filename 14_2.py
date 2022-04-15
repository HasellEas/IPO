class childe():
    def getIncome(self):
        return self.middle_income
    def getOutcome(self):
        return self.middle_outcome
    def setIncome(self, new):
        self.middle_income = new
    def setOutcome(self, new):
        self.middle_Outcome = new
    def getAge(self):
        return self.age
    def getFio(self):
        return self.fio
    def getSex(self):
        return self.sex
class schoolchild():
    def schoolstart(self):
        print(self.fio+", вы стали учеником")
        self.age = 6
        self.middle_income = 200
        self.middle_outcome = 50
    def lesson(self):
        print("Проходит урок...")
    def ege(self):
        print("Вы выпустились!")
class student():
    def studentstart(self):
        print(self.fio+", вы стали студентом")
        self.age = 15
        self.middle_income = 400
        self.middle_outcome = 100
    def para(self):
        print("Проходит пара...")
    def end(self):
        print("Вы окончили колледж")
class worker():
    def workerstart(self):
        print(self.fio+", вы стали рабочим")
        self.age = 19
        self.middle_income = 900
        self.middle_outcome = 700
    def work(self):
        print("Вы работаете...")
    def die(self):
        print("Вы умерли XD")
        self.age = 75
class life(worker, student, schoolchild, childe):
    def __init__(self, fio, age, sex):
        print("Вы родились")
        self.fio = fio
        self.age = age
        self.sex = sex
        self.middle_income = 0
        self.middle_outcome = 0

born = life("Иванов Иван Иванович", 1, 1)
print(born.getAge())
print(born.getSex())
print(born.getFio())
print(born.getIncome())
print(born.getOutcome())
born.schoolstart()
born.lesson()
born.ege()
print(born.getAge())
print(born.getSex())
print(born.getFio())
print(born.getIncome())
print(born.getOutcome())
born.studentstart()
born.para()
born.end()
print(born.getAge())
print(born.getSex())
print(born.getFio())
print(born.getIncome())
print(born.getOutcome())
born.workerstart()
born.work()
print(born.getAge())
print(born.getSex())
print(born.getFio())
print(born.getIncome())
print(born.getOutcome())
born.die()
print(born.getAge())