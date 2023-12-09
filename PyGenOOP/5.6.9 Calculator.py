class Calculator:
    def __call__(self, num_1, num_2, operation):
        if num_2 == 0 and operation == '/':
            raise ValueError('Деление на ноль невозможно')
        res = eval(f"{num_1}{operation}{num_2}")
        return res
