class Gun:
    def __init__(self):
        self.counter = 0
        self.sounds = ('pif', 'paf')

    def shoot(self):
        print(self.sounds[self.counter % 2])
        self.counter += 1
