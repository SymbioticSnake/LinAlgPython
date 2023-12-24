class Matrix:
    def __init__(self, rows=2, columns=2):
        self.m = rows
        self.n = columns
        self.matrix = [[0 for _ in range(self.n)] for _ in range(self.m)]

    def __add__(self, other):
        if other.m != self.m or other.n != self.n:
            print("Cannot add matrices")
            return self

        newMatrix = Matrix(self.m, self.n)

        for i in range(self.m):
            for j in range(self.n):
                newMatrix.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]

        return newMatrix

    def __sub__(self, other):
        if other.m != self.m or other.n != self.n:
            print("Cannot add matrices")
            return self

        newMatrix = Matrix(self.m, self.n)

        for i in range(self.m):
            for j in range(self.n):
                newMatrix.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]

        return newMatrix

    def __str__(self):
        string = ""

        for row in range(self.m):
            string += "["

            for col in range(self.n):
                string += str(self.matrix[row][col])
                if col != self.n-1:
                    string += ", "

            string += "]"
            if row != self.m-1:
                string += "\n"

        string += "\n"
        return string

    def enter_matrix(self):
        for i in range(self.m):
            for j in range(self.n):
                entry = float(input("Enter entry for (" + str(i+1) + ", " + str(j+1) + "): "))
                self.matrix[i][j] = entry

    def file_matrix(self, fin):
        for i in range(self.m):
            fileLine = fin.readline().split()
            for j in range(self.n):
                self.matrix[i][j] = float(fileLine[j])