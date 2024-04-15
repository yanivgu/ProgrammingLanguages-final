from abstraction.expression import Expression
import scope
import re

class PrintScopeVariables(Expression):
    pattern = r"^print_scope_variables\s*\(\s*\)\s*$"
    prefix = r"^print_scope_variables\s*"

    def evaluate(self):
        for variable in scope.variables:
            print(variable + ": " + str(scope.variables[variable]))

    def __str__(self):
        return "print_scope_variables(" + str(self.expression) + ")"
    
    def check_command(expression):
        return re.match(PrintScopeVariables.pattern, expression) is not None
    
    def check_prefix(expression):
        return re.match(PrintScopeVariables.prefix, expression) is not None