variables = { 0: {"__scope_type": "global"}}
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

def increment_scope(scope_type):
    level += 1
    variables[level] = {"__scope_type": scope_type}

def decrement_scope(scope_type):
    if (level == 0):
        raise ValueError("Cannot decrement scope below 0")
    if (variables[level]["__scope_type"] != scope_type):
        raise ValueError("Invalid scope type")
    variables.pop(level)
    level -= 1
