from math import cos, sin, exp
class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    def __mul__(self, other):
        re = self.real * other.real - self.imaginary * other.imaginary
        im = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(re, im)
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
    def __truediv__(self, other):
        tmp = self * other.conjugate()
        divisor = float(other.real**2 + other.imaginary**2)
        return ComplexNumber(tmp.real / divisor, tmp.imaginary / divisor)
    def __abs__(self):
        return pow(self.real ** 2 + self.imaginary ** 2, 0.5)
        pass
    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)
    def exp(self):
        r = round(cos(self.imaginary), 8) * exp(self.real)
        i = round(sin(self.imaginary), 8) * exp(self.real)
        return ComplexNumber(r, i)