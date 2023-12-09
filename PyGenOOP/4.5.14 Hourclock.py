class HourClock:
    def __init__(self, hours):
        if not(isinstance(hours, int) and 1 <= hours <= 12):
            raise ValueError('Некорректное время')
        self.hours = hours

    def get_hours(self):
        return self._hours

    def set_hours(self, hours):
        if not (isinstance(hours, int) and 1 <= hours <= 12):
            raise ValueError('Некорректное время')
        self._hours = hours

    hours = property(get_hours, set_hours)
