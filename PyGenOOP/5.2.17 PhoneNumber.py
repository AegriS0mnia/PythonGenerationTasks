class PhoneNumber:
    def __init__(self, phonenumber):
        self.phonenumber = phonenumber.replace(' ', '')

    def __repr__(self):
        return f"PhoneNumber('{self.phonenumber}')"

    def __str__(self):
        return f'({self.phonenumber[:3]}) {self.phonenumber[3: 6]}-{self.phonenumber[6:]}'
