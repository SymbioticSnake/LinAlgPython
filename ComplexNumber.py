"""
Contains a ComplexNumber class that parses complex numbers.
"""

from math import *


class ComplexNumber:
    def __init__(self, real=0.0, imaginary=0.0):
        self.real = round(real, 6)
        self.imaginary = round(imaginary, 6)

    def __str__(self):
        return "({}) + ({}) j".format(self.real, self.imaginary)

    def __repr__(self):
        return "({}) + ({}) j".format(self.real, self.imaginary)

    def get_real(self): return self.real

    def get_imaginary(self): return self.imaginary

    def argument(self): return atan2(self.imaginary, self.real)

    def modulus(self): return sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self): return ComplexNumber(self.real, -self.imaginary)

    def set_real(self, real):
        self.real = real

    def set_imaginary(self, imaginary):
        self.imaginary = imaginary

    def __power(self, power):
        return ComplexNumber(self.modulus() ** power * cos(power * self.argument()),
                             self.modulus() ** power * sin(power * self.argument()))

    # Given an integer power n, the function returns a tuple containing all the n-th roots
    # of the current complex number.
    def __root(self, power):
        n = int(1/power)
        return tuple(ComplexNumber(self.modulus() ** (1/n) * cos((self.argument() + 2*k*pi) / n),
                                   self.modulus() ** (1/n) * sin((self.argument() + 2*k*pi) / n))
                     for k in range(int(n)))

    def exp_form(self):
        return "{}e^(j*{})".format(self.modulus(), self.argument())

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return ComplexNumber(self.real * other, self.imaginary * other)
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                             self.real * other.imaginary + other.real * self.imaginary)

    def __truediv__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return ComplexNumber(self.real / other, self.imaginary / other)
        return ComplexNumber(self.real, self.imaginary) * other.conjugate() / (other.real**2 + other.imaginary**2)

    def __pow__(self, power):
        if power == 0:
            return ComplexNumber(1, 0)
        elif 0 < power < 1:
            return self.__root(power)
        else:
            return self.__power(power)
