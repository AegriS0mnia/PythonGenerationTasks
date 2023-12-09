def pluck(data, path, default=None):
    if isinstance(path, str):
        path = path.split('.')

    for key in data:
        if key == path[0]:
            if isinstance(data[key], dict):
                path = path[1:]
                if path:
                    return pluck(data[key], path, default=default)
                else:
                    return data[key]
            else:
                return data[key]
    return default
