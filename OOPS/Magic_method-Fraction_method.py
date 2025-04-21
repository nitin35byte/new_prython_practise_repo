class Fraction:

    def __init__(self,x,y):
        self.num= x
        self.den= y
    def __str__(self):
        return '{}/{}'.format(self.num , self.den)

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
    def __sub__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den

fr1 = Fraction(2,5)
fr2= Fraction(3,7)
print(fr1 + fr2)