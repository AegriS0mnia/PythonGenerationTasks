class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.root_of_discriminant = (b**2 - 4*a*c)**0.5

    @property
    def x1(self):
        if self.root_of_discriminant >= 0:
            root = (-self.b - self.root_of_discriminant) / (2*self.a)
            return root
        else:
            return None

    @property
    def x2(self):
        if self.root_of_discriminant >= 0:
            root = (-self.b + self.root_of_discriminant) / (2*self.a)
            return root
        else:
            return None

    @property
    def view(self):
        if self.b >= 0 and self.c >= 0:
            return f'{self.a}x^2 + {self.b}x + {self.c}'
        elif self.b >= 0 and self.c < 0:
            return f'{self.a}x^2 + {self.b}x - {abs(self.c)}'
        elif self.b < 0 and self.c >= 0:
            return f'{self.a}x^2 - {abs(self.b)}x + {abs(self.c)}'
        elif self.b < 0 and self.c < 0:
            return f'{self.a}x^2 - {abs(self.b)}x - {abs(self.c)}'

    @property
    def coefficients(self):
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, coefficients):
        self.a, self.b, self.c = coefficients
        self.root_of_discriminant = (self.b**2 - 4*self.a*self.c)**0.5

# TEST_8:
polynom = QuadraticPolynomial(500, -601, 101)

print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

print()

polynom.coefficients = (-1000, 1202, -202)
print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)
