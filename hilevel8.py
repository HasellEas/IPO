class TriangleChecker():
    def is_triangle(self, a, b, c):
        for __ in [a,b,c]:
            if type(__) != int:
                return "Нужно вводить только числа!"
            if __ < 0:
                return "С отрицательными числами ничего не идёт!"
        maximal_part = max([a,b,c])
        array = [a,b,c]
        array.pop(array.index(maximal_part))
        x = 0
        for __ in array:
            x+= __ 
        if x>maximal_part: 
            return "Ура. Треугольник можно построить!"
        else:
            return "Жаль. Ничего невыйдет."

q = TriangleChecker()
print(q.is_triangle(1,6,6))