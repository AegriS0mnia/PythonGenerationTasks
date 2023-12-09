class Strip:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, string):
        while string[0] in self.chars or string[-1] in self.chars:
            for c in self.chars:
                while string.startswith(c):
                    string = string[1:]
                while string.endswith(c):
                    string = string[:-1]
        return string
