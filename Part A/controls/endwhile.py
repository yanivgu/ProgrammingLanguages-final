from abstraction import Expression
import scope
import re

class EndWhile(Expression):
    pattern = r"^endwhile\s*$"
    prefix = r"^endwhile\s*"

    def evaluate(self):
        scope.decrement_scope("while")

    def __str__(self):
        return "endwhile"

    def check_command(expression):
        return re.match(EndWhile.pattern, expression) is not None

    def check_prefix(expression):
        return re.match(EndWhile.prefix, expression) is not None