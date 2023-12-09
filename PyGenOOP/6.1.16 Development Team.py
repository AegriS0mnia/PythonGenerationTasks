class DevelopmentTeam:
    def __init__(self):
        self.juniors = []
        self.seniors = []

    def add_junior(self, *args):
        self.juniors += args

    def add_senior(self, *args):
        self.seniors += args

    def __iter__(self):
        for jun in self.juniors:
            yield (jun, 'junior')
        for sen in self.seniors:
            yield (sen, 'senior')
