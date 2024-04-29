from abstraction import Expression
import scope
import re

class Variable(Expression):
    pattern = r"^[a-zA-Z][a-zA-Z0-9_]{0,19}$"
    
    def __init__(self, value):
        self.variable_name = re.match(Variable.pattern, value.strip())[0]
        
    def evaluate(self):
        return scope.try_get_value(self.variable_name)
    
    def __str__(self):
        return str(self.variable_name)
    
    def check_expression(expression):
        return re.match(Variable.pattern, expression.strip()) is not None
    
    def set_value(self, value):
        return scope.set_value(self.variable_name, value)