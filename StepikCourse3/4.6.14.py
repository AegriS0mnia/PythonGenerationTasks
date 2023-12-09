import pickle


def filter_dump(filename, objects, typename):
    filtered_objects = list(filter(lambda obj: type(obj) == typename, objects))
    with open(filename, 'wb') as output:
        pickle.dump(filtered_objects, output)
