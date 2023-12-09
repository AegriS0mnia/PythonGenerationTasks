from datetime import date

def date_formatter(country_code):
    def reformatte_date(today):
        formattes = {'ru': '%d.%m.%Y', 'us': '%m-%d-%Y', 'ca': '%Y-%m-%d',
                     'br': '%d/%m/%Y', 'fr': '%d.%m.%Y', 'pt': '%d-%m-%Y'}
        return date.strftime(today, formattes[country_code])
    return reformatte_date

