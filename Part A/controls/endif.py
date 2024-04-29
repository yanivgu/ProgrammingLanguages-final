from abstraction import Expression
import scope
import re

class EndIf(Expression):
    pattern = r"^endif\s*$"
    prefix = r"^endif\s*"

    def evaluate(self):
        scope.end_scope("if")

    def __str__(self):
        return "endif"

    def check_command(expression):
        return re.match(EndIf.pattern, expression) is not None

    def check_prefix(expression):
        return re.match(EndIf.prefix, expression) is not None