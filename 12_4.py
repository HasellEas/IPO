class Point:
    def __init__(self, xy):
        self.xy = xy
    def setX(self, x):
        self.xy = (x, self.xy[1])
    def setY(self, y):
        self.xy = (self.xy[0], y)
    def set(self, xy):
        self.xy = xy
    def getX(self):
        return self.xy[0]
    def getY(self):
        return self.xy[1]
    def get(self):
        return self.xy          

p = Point((12,5))
print(p.get())
print(p.getX())
print(p.getY())
p.setX(2)
p.setY(9)
print(p.get())
print(p.getX())
print(p.getY())