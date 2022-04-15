class mainobject():
    def __init__(self, x):
        self.x = x
    @property
    def storage(self):
        return self.x
    @storage.deleter
    def storage(self):
        del self.x
    @storage.setter
    def storage(self, x):
        self.x = x

thread = mainobject(6)
print(thread.storage)
thread.storage = 8
print(thread.storage)
del thread.storage