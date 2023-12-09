def get_all_values(nested_dicts, key):
    ans = set()
    if key in nested_dicts:
        ans.add(nested_dicts[key])
        return nested_dicts[key]

    for v in nested_dicts.values():
        if type(v) == dict:
            value = get_all_values(v, key)
            if value is not None:
                return value

    return ans

my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print(*sorted(result))
