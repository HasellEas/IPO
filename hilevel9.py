class plant():
    def __init__(self, plant_index, plant_stage):
        self.plant_stage = plant_stage
        self.plant_index = plant_index
        self.objects = []
    def get_plant(self):
        return (self.plant_index, self.plant_stage)
    def add(self, data):
        self.objects.append(data)
    def get(self):
        return self.objects

class worker():
    def __init__(self,name,plant_index):
        self.name = name
        self.plant_index = plant_index
    def get_name(self):
        return self.name
    def get_plant_index(self):
        return self.plant_index

class tomato():
    def __init__(self, index, stage, owner, plants):
        self.index = index
        self.stage = stage
        self.plants = plants
        self.owner = owner
        self.stage_names = ["Отсутсвует","Цветение","Зелёный","Красный"]
    def grow(self):
        if self.stage >= 4:
            return False
        else:
            self.stage += 1
            return True
    def get(self):
        return (self.index, self.stage, self.stage_names, (self.plants[0],self.plants[1]), (self.owner[0],self.owner[1]))

__ = plant(1,1)
human = worker("Вася", 1)
for i in range(0,5):
    __.add(tomato(i, 1, (human.get_name(), human.get_plant_index()),__.get_plant()))
ent = __.get()
ent[0].grow()
for sub in ent:
    print(sub.get())