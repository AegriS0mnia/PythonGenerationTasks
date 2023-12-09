class Color:
    def __init__(self, hexcode):
        self._hexcode = hexcode
        self.r = int(hexcode[:2], 16)
        self.g = int(hexcode[2: 4], 16)
        self.b = int(hexcode[4:], 16)

    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, new_hexcode):
        self._hexcode = new_hexcode
        self.r = int(new_hexcode[:2], 16)
        self.g = int(new_hexcode[2: 4], 16)
        self.b = int(new_hexcode[4:], 16)
