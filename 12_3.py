class StringVar:
    def __init__(self, n):
        self.n = n
    def set(self, n):
        self.n = n
    def get(self):
        return self.n

num = StringVar(12)
print(num.get())
num.set(13)
print(num.get())