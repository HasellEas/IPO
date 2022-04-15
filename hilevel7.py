import datetime

class Paragoda():
    def __init__(self, nazv, temp, vlag, osadok):
        self.nazv = nazv
        self.temp = temp
        self.vlag = vlag
        self.osadok = osadok

    def getdate(self):
        __ = datetime.datetime.now().day
        return __ 

    def inform(self):
        if self.temp <=10: status = "холодно" 
        elif self.temp >10 and self.temp <= 25: status = "тепло" 
        else: status = "жарко"
        print("Предупреждение! "+self.nazv+" "+str(self.getdate())+" числа будет "+status+", темпиратура будет составлять: "+str(self.temp)+" *С\nВлажность воздуха: "+str(self.vlag)+"%\nКоличество остадков: "+str(self.osadok)+"мл")

__ = Paragoda("Весной", 9, 60, 20)
__.inform()