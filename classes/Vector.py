from Matrix import *


class Vector(Matrix):
    def __init__(self, m=2):
        Matrix.__init__(self, m, 1)
        self.matrix = [[0] for _ in range(m)]

    def __add__(self, other):
        if other.m != self.m:
            print("Cannot add")
            return self

        new_vector = Vector(self.m)

        for i in range(self.m):
            new_vector.matrix[i][0] = self.matrix[i][0] + other.matrix[i][0]

        return new_vector

    def __sub__(self, other):
        if other.m != self.m:
            print("Cannot subtract")
            return self

        new_vector = Vector(self.m)

        for i in range(self.m):
            new_vector.matrix[i][0] = self.matrix[i][0] - other.matrix[i][0]

        return new_vector

    def __mul__(self, other):
        if type(other) is not int:
            print("Cannot multiply")
            return self
        else:
            new_vector = Vector(self.m)
            new_vector.matrix = [[other * self.matrix[i][0]] for i in range(self.m)]

        return new_vector

    def enter_vector(self):
        for i in range(self.m):
            entry = input("Enter entry #{}: ".format(i+1))
            self.matrix[i][0] = float(entry)
