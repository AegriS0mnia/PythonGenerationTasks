from datetime import date

class DateFormatter:
    def __init__(self, country_code):
        self.country_code = country_code

    def __call__(self, date):
        country_codes = {'ru': '%d.%m.%Y', 'us': '%m-%d-%Y', 'ca': '%Y-%m-%d', 'br': '%d/%m/%Y', 'fr': '%d.%m.%Y',
                         'pt': '%d-%m-%Y'}

        return date.strftime(country_codes[self.country_code])
