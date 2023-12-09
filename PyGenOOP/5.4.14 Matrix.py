class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.matrix = [[value]*cols for i in range(rows)]

    def get_value(self, row, col):
        return self.matrix[row][col]

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def __repr__(self):
        return f"Matrix{self.rows, self.cols}"

    def __str__(self):
        return '\n'.join([' '.join(map(str, i)) for i in self.matrix])

    def copy(self, func=lambda x: x, transpose=False):
        if transpose:
            matrix = Matrix(self.cols, self.rows)
        else:
            matrix = Matrix(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                value = func(self.get_value(row, col))
                if transpose:
                    matrix.set_value(col, row, value)
                else:
                    matrix.set_value(row, col, value)
        return matrix

    def __pos__(self):
        return self.copy()

    def __neg__(self):
        return self.copy(func=lambda x: -x)

    def __invert__(self):
        return self.copy(transpose=True)

    def __round__(self, n=None):
        return self.copy(func=lambda x: round(x, n))

