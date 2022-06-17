"""
реализовать операцию над дробью, то есть создать класс Fraction
у него будет 2 атрибута (numertor, denumerator)
сделать add, sub, mul, floordiv (Dunder Methods) по правилам математики!)
"""


class Fraction:

    def __init__(self, numerator, denumerator):
        self.num = numerator
        self.denum = denumerator

    def __str__(self):
        return str(self.num) + "/" + str(self.denum)

    def __add__(self, other):
        new_num = self.num * other.denum + self.denum * other.num
        new_denum = self.denum * other.denum
        return Fraction(new_num, new_denum)

    def __sub__(self, other):
        new_num = self.num * other.denum - self.denum * other.num
        new_denum = self.denum * other.denum
        return Fraction(new_num, new_denum)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_denum = self.denum * other.denum
        return Fraction(new_num, new_denum)

    def __floordiv__(self, other):
        new_num = self.num * other.denum
        new_denum = self.denum * other.num
        return Fraction(new_num, new_denum)


x = Fraction(4, 6)
y = Fraction(5, 7)

print(f'{x} + {y} = {x+y}')
print(f'{x} - {y} = {x-y}')
print(f'{x} * {y} = {x*y}')
print(f'{x} // {y} = {x//y}')

