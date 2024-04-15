from data_types import Integer, Variable
from commands import Print
from operators import Add, Sub, Mul, Div, Equal

def interpret(code):
    code = code.strip()
    if Add.check_expression(code):
        parts = Add.split(code)
        return Add(interpret(parts[0]), interpret(parts[1]))
    elif Sub.check_expression(code):
        parts = Sub.split(code)
        return Sub(interpret(parts[0]), interpret(parts[1]))
    elif Mul.check_expression(code):
        parts = Mul.split(code)
        return Mul(interpret(parts[0]), interpret(parts[1]))
    elif Div.check_expression(code):
        parts = Div.split(code)
        return Div(interpret(parts[0]), interpret(parts[1]))
    elif Integer.check_expression(code):
        return Integer(code)
    else:
        raise ValueError("Invalid operator", code)

code = ""
while (code.strip() != "exit"):
    code = input(">>> ")
    if code != "exit":
        try:
            result = interpret(code)
            print(result.evaluate())
        except ValueError as e:
            print(e)
