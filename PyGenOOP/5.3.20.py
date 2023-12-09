from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, version):
        self.version = version
        self.version_list = list(map(int, version.split('.')))
        while len(self.version_list) < 3:
            self.version_list += [0]

    def __repr__(self):
        return f"Version('{'.'.join(map(str, self.version_list))}')"

    def __str__(self):
        return '.'.join(map(str, self.version_list))

    def __eq__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        while len(other.version_list) < 3:
            other.version_list += [0]
        return self.version_list == other.version_list

    def __gt__(self, other):
        if isinstance(other, Version):
            return self.version_list > other.version_list
        return NotImplemented

