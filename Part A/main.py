from validators.variable_name_validator import validate_variable_name
from data_types import Integer, Variable
from commands import Print
from operators import Add, Sub, Mul, Div, Equal

import re
class Interpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, code):
        tokens = code.split(' ')

        if (tokens[0] == "print"):
            variable = tokens[1]
            if variable not in self.variables:
                raise ValueError("Variable not found")
            print(self.variables[variable])
            return

        if tokens[1] != "=":
            raise ValueError("Invalid assignment")

        variable = tokens[0]

        validate_variable_name(variable)

        operator = tokens[2]
        value = int(tokens[3])

        if operator == "+":
            self.variables[variable] = self.variables.get(variable, 0) + value
        elif operator == "-":
            self.variables[variable] = self.variables.get(variable, 0) - value
        elif operator == "*":
            self.variables[variable] = self.variables.get(variable, 0) * value
        elif operator == "/":
            self.variables[variable] = self.variables.get(variable, 0) / value
        else:
            raise ValueError("Invalid operator")

        return self.variables[variable]

expression = "  3 * 5       "
parts = Mul.split(expression)
a = Mul(Integer(parts[0]), Integer(parts[1]))
print(a)
print(a.evaluate())

exit()
code = ""
interpreter = Interpreter()
while (code.strip() != "exit"):
    code = input(">>> ")
    if code != "exit":
        try:
            result = interpreter.interpret(code)
        except ValueError as e:
            print(e)
