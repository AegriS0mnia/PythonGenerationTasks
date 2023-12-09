def get_id(names, name):
    if isinstance(name, str):
        if name.isalpha() and name == name.lower().capitalize():
            names.append(name)
            return len(names)
        else:
            raise ValueError('Имя не является корректным')
    else:
        raise TypeError('Имя не является строкой')
