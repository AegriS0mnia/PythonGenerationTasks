class AnyClass:
    def __init__(self, **kwargs):
        self.attrs_string = ', '.join([f"{attr}={repr(value)}" for attr, value in kwargs.items()])
        for key, item in kwargs.items():
            setattr(self, key, item)

    def __repr__(self):
        return f"AnyClass({self.attrs_string})"

    def __str__(self):
        return f"AnyClass: {self.attrs_string}"
