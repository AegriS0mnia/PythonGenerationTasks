import functools


@functools.total_ordering
class RomanNumeral:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number

    @staticmethod
    def to_int(number):
        ans = 0
        convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ints = [convert[i] for i in number]
        if len(number) == 1:
            return convert[number]

        while len(ints) >= 2:
            if ints[0] < ints[1]:
                ans -= ints[0]
            else:
                ans += ints[0]
            ints = ints[1:]
            if len(ints) == 1:
                ans += ints[0]
                break
        return ans

    @staticmethod
    def to_roman(number):
        ans = ''
        all_roman = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9,
                     'V': 5, 'IV': 4, 'I': 1}
        while number > 0:
            for sign in all_roman:
                if number - all_roman[sign] >= 0:
                    number -= all_roman[sign]
                    ans += sign
                    break
        return ans

    def __int__(self):
        ans = self.to_int(self.number)
        return ans

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            ans = self.to_int(self.number) == self.to_int(other.number)
            return ans
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, RomanNumeral):
            ans = self.to_int(self.number) > self.to_int(other.number)
            return ans
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            ans = RomanNumeral(self.to_roman(self.to_int(self.number) + self.to_int(other.number)))
            return ans
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            ans = RomanNumeral(self.to_roman(self.to_int(self.number) - self.to_int(other.number)))
            return ans
        return NotImplemented

