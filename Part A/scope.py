variables = {}

def try_get_value(name):
    if name not in variables:
        raise ValueError(str.format("Variable {} not found", name))
    return variables[name]

def set_value(name, value):
    variables[name] = value
    return value