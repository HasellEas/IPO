class krug():
    def get_krugsqr(self, a):
        return 3.14*a**2
    def get_krugperim(self, a):
        return 3.14*a
class kub():
    def get_kubsqr(self, a):
        return a*a
    def get_kubperim(self, a):
        return 4*a
class treug():
    def get_treugsqr(self, a, b):
        return (a*b)/2
    def get_treugperim(self, a, b, c):
        return a+b+c
class math(krug, kub, treug):
    pass

m = math()

print(m.get_kubsqr(5))
print(m.get_kubperim(5))

print(m.get_krugsqr(5))
print(m.get_krugperim(5))

print(m.get_treugsqr(5,6))
print(m.get_treugperim(5,3,6))