from data_types import *
from commands import *
from controls import *
from operators import *
from comment import *
import scope

def execute_while_loop(while_scope: WhileLoop):
    condition = while_scope.get_condition()
    lines = while_scope.get_lines()
    while (condition.evaluate() == 1):
        for line in lines:
            execute_line(line, 0)

def execute_line(line: str, line_number):
    if line.strip() != "exit()":
        try:
            result = __interpret(line, 0, line_number)
            if result is not None:
                result.evaluate()
            return 1
        except ValueError as e:
            print(e, line_number)
            return -1
    return 0

def __interpret(line: str, recurse_level, line_number):
    line = remove_comments(line)
    line = line.strip()
    next_recurse_level = recurse_level + 1

    if scope.is_while_scope():
        while_scope = scope.get_while_object()
        is_first_pass = while_scope.is_first_pass()
        is_endwhile = EndWhile.check_command(line)
        if is_first_pass and not is_endwhile and recurse_level == 0:
            while_scope.add_line(line)
            
        if is_endwhile:
            while_scope.end_while_inspection()
            execute_while_loop(while_scope)
            top_while_scope = scope.get_top_while_scope()
            if top_while_scope is not None and top_while_scope.is_first_pass():
                for loop_line in while_scope.get_lines():
                    top_while_scope.add_line(loop_line)
                #top_while_scope.add_line('endwhile')
        
    if scope.is_skipping_if():
        if EndIf.check_command(line):
            scope.end_scope("if")
        else:
            return None
    elif IfThen.check_prefix(line):
        if not IfThen.check_command(line):
            raise ValueError("Invalid if_then statement", line)
        internal_condition = IfThen.extract_condition(line)
        return IfThen(__interpret(internal_condition, next_recurse_level, line_number), line_number)
    elif EndIf.check_prefix(line):
        if not EndIf.check_command(line):
            raise ValueError("Invalid endif statement", line)
        return EndIf()
    elif WhileLoop.check_prefix(line):
        if not WhileLoop.check_command(line):
            raise ValueError("Invalid while_loop statement", line)
        internal_condition = WhileLoop.extract_condition(line)
        return WhileLoop(__interpret(internal_condition, next_recurse_level, line_number), line_number)
    elif EndWhile.check_prefix(line):
        if not EndWhile.check_command(line):
            raise ValueError("Invalid endwhile statement", line)
        return EndWhile()
    elif PrintScopeVariables.check_prefix(line):
        if not PrintScopeVariables.check_command(line):
            raise ValueError("Invalid print_scope_variables statement", line)
        return PrintScopeVariables()
    elif Print.check_prefix(line):
        if not Print.check_command(line):
            raise ValueError("Invalid print statement", line)
        internal_expression = Print.extract_expression(line)
        return Print(__interpret(internal_expression, next_recurse_level, line_number))
    elif Comparison.check_expression(line):
        parts = Comparison.split(line)
        operator = Comparison.extract_operator(line)
        return Comparison(__interpret(parts[0], next_recurse_level, line_number), __interpret(parts[1], next_recurse_level, line_number), operator)
    elif Equal.check_expression(line):
        parts = Equal.split(line)
        return Equal(__interpret(parts[0], next_recurse_level, line_number), __interpret(parts[1], next_recurse_level, line_number))
    elif Add.check_expression(line):
        parts = Add.split(line)
        return Add(__interpret(parts[0], next_recurse_level, line_number), __interpret(parts[1], next_recurse_level, line_number))
    elif Sub.check_expression(line):
        parts = Sub.split(line)
        return Sub(__interpret(parts[0], next_recurse_level, line_number), __interpret(parts[1], next_recurse_level, line_number))
    elif Mul.check_expression(line):
        parts = Mul.split(line)
        return Mul(__interpret(parts[0], next_recurse_level, line_number), __interpret(parts[1], next_recurse_level, line_number))
    elif Div.check_expression(line):
        parts = Div.split(line)
        return Div(__interpret(parts[0], next_recurse_level, line_number), __interpret(parts[1], next_recurse_level, line_number))
    elif Integer.check_expression(line):
        return Integer(line)
    elif Variable.check_expression(line):
        return Variable(line)
    elif line.strip() == "" and recurse_level == 0:
        return None
    else:
        raise ValueError("Invalid operator", line)