def fib(number):
    return (lambda number: 1 if number <= 2 else fib(number - 1) + fib(number - 2))(number)

