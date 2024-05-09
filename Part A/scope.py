variables = { 0: {"__scope_type": "global"}}
while_scope_levels = []
level = 0

def try_get_value(name):
    for i in range(level, -1, -1):
        #print(variables[i])
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

def set_new_scope(scope_type, line_number, **kwargs):
    global level
    level += 1
    variables[level] = {"__scope_type": scope_type, "__line_number": line_number, **kwargs}
    if scope_type == "while":
        while_scope_levels.append(level)

def end_scope(scope_type):
    global level
    if (level == 0):
        raise ValueError("Cannot decrement scope below 0")
    if (variables[level]["__scope_type"] != scope_type):
        raise ValueError("Invalid scope type")
    if (scope_type == "while"):
        while_scope_levels.pop()
    variables.pop(level)
    level -= 1

def is_skipping_if() -> bool:
    return level > 0 and variables[level]["__scope_type"] == "if" and not variables[level]["__condition_state"]

def is_while_scope() -> bool:
    return len(while_scope_levels) > 0

def get_while_object():
    while_level =  while_scope_levels[-1]
    return variables[while_level]["__while_object"]

def get_top_while_scope():
    if len(while_scope_levels) < 2:
        return None
    else:
        return variables[while_scope_levels[-2]]["__while_object"]
