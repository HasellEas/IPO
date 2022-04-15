class mathmain():
    def __init__(self):
        self.num = 0
    @property
    def countm(self):
        return self.num
    @countm.setter
    def countm(self, nums):
        exec("self.num = "+nums)

mat = mathmain()
mat.countm = "1+1"
print(mat.countm)