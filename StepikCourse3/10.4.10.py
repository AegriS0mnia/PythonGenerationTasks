class Fibonacci:
    def __init__(self):
        self.num_1 = 0
        self.num_2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.num_1, self.num_2 = self.num_2, self.num_1 + self.num_2
        return self.num_1
