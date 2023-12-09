from collections import namedtuple
from typing import NoReturn


class Postman:
    def __init__(self):
        self.delivery_data = []
        self.Address = namedtuple('Address', ['street', 'house', 'flat'])

    def add_delivery(self, street, house, flat) -> NoReturn:
        address = self.Address(street, house, flat)
        self.delivery_data.append(address)

    def get_houses_for_street(self, street) -> list[int]:
        houses: list[int] = []
        [houses.append(adr.house) for adr in self.delivery_data if adr.street == street and adr.house not in houses]

        return houses

    def get_flats_for_house(self, street, house) -> list[int]:
        flats: list[int] = [adr.flat for adr in self.delivery_data if adr.street == street and adr.house == house]

        return flats
