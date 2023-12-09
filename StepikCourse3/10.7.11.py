def txt_to_dict():
    with open('planets.txt', encoding='utf-8') as text_file:
        lines = (i.rstrip() for i in text_file.read().split('\n\n') if i.rstrip())
        separated_values = (i.split('\n') for i in lines)
        for planet_info in separated_values:
            _dict = {}
            for line in planet_info:
                _dict.setdefault(*line.split(' = '))
            yield _dict
