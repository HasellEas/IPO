lister = {"w":"","g":"","e":""}
for __ in lister.items():
    lister[__[0]]=input()
class main():
    def check(self, data, name):
        for __ in data.items():
            if __[1] == name:
                return __[0]

__ = main()
print(__.check(lister, input()))