from data_types import Integer, Variable
from commands import Print, PrintScopeVariables
from operators import Add, Sub, Mul, Div, Equal
from comment import *


def interpret(line):
    return __interpret(line, 0)

def __interpret(line, recurse_level):
    line = remove_comments(line)
    line = line.strip()
    next_recurse_level = recurse_level + 1

    if PrintScopeVariables.check_prefix(line):
        if not PrintScopeVariables.check_command(line):
            raise ValueError("Invalid print_scope_variables statement", line)
        return PrintScopeVariables()
    elif Print.check_prefix(line):
        if not Print.check_command(line):
            raise ValueError("Invalid print statement", line)
        internal_expression = Print.extract_expression(line)
        return Print(__interpret(internal_expression, next_recurse_level))
    elif Equal.check_expression(line):
        parts = Equal.split(line)
        return Equal(__interpret(parts[0], next_recurse_level), __interpret(parts[1], next_recurse_level))
    elif Add.check_expression(line):
        parts = Add.split(line)
        return Add(__interpret(parts[0], next_recurse_level), __interpret(parts[1], next_recurse_level))
    elif Sub.check_expression(line):
        parts = Sub.split(line)
        return Sub(__interpret(parts[0], next_recurse_level), __interpret(parts[1], next_recurse_level))
    elif Mul.check_expression(line):
        parts = Mul.split(line)
        return Mul(__interpret(parts[0], next_recurse_level), __interpret(parts[1], next_recurse_level))
    elif Div.check_expression(line):
        parts = Div.split(line)
        return Div(__interpret(parts[0], next_recurse_level), __interpret(parts[1], next_recurse_level))
    elif Integer.check_expression(line):
        return Integer(line)
    elif Variable.check_expression(line):
        return Variable(line)
    elif line.strip() == "" and recurse_level == 0:
        return None
    else:
        raise ValueError("Invalid operator", line)