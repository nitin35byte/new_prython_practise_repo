def flatten_dict(d, parent_key='', sep='_'):
    flat_dict = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            flat_dict.update(flatten_dict(v, new_key, sep))
        else:
            flat_dict[new_key] = v
    return flat_dict
data = {'a': {'x': 10, 'y': 20}, 'b': {'z': 30}}

print(flatten_dict(data))
