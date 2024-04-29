from abstraction import Expression
import re

int_max_value = 2147483647
int_min_value = -2147483648

class Integer(Expression):
    pattern = r"^\d+$"
    
    def __init__(self, value):
        regex_result = re.match(Integer.pattern, value.strip())
        if regex_result is None:
            raise ValueError("Invalid integer", value)
        self.value = int(regex_result[0])

    def evaluate(self):
        result = int(self.value)
        if result > int_max_value or result < int_min_value:
            raise ValueError("Integer overflow", self.value)
        return result

    def __str__(self):
        return str(self.value)
    
    def check_expression(expression):
        return re.match(Integer.pattern, expression.strip()) is not None