def sourcetemplate(url):
    def get_valid_url(**kwargs):
        query_string = [f'{key}={value}' for key, value in sorted(kwargs.items(), key=lambda x: x[0])]
        query_string = '&'.join(query_string)
        if query_string:
            return url + '?' + query_string
        else:
            return url

    return get_valid_url
