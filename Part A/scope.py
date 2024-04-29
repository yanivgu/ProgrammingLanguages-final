variables = { 0: {}}
level = 0

def try_get_value(name):
    for i in range(level, -1, -1):
        if name in variables[i]:
            return variables[i][name]
    raise ValueError(str.format("Variable {} not found", name))

def set_value(name, value):
    for i in range(level, -1, -1):
        if name in variables[i]:
            variables[i][name] = value
            return value

    variables[level][name] = value
    return value

def increment_scope():
    level += 1
    variables[level] = {}

def decrement_scope():
    if (level == 0):
        raise ValueError("Cannot decrement scope below 0")
    variables.pop(level)
    level -= 1
