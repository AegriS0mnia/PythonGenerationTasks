class IPAddress:

    def __init__(self, ipaddress):
        self.ipaddress = ipaddress

    def __repr__(self):
        if isinstance(self.ipaddress, str):
            return f"IPAddress('{self.ipaddress}')"
        else:
            return f"IPAddress('{'.'.join(map(str, self.ipaddress))}')"

    def __str__(self):
        if isinstance(self.ipaddress, str):
            return self.ipaddress
        else:
            return '.'.join(map(str, self.ipaddress))
