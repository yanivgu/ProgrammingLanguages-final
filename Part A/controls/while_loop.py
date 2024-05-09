from abstraction import Expression
import scope
import re

class WhileLoop(Expression):
    pattern = r"^while\s+.+\s*$"
    prefix = r"^while\s+"

    def __init__(self, condition: Expression, line_number: int):
        self.condition = condition
        self.line_number = line_number
        self.lines = []

    def evaluate(self):
        if self.condition.evaluate():
            scope.set_new_scope("while", self.line_number, __while_object = self)
            self.in_inspection = True
        return None

    def __str__(self):
        return "while " + str(self.condition)

    def extract_condition(expression):
        condition = expression[expression.find("while") + 5:len(expression)]
        return condition

    def check_command(expression):
        return re.match(WhileLoop.pattern, expression) is not None

    def check_prefix(expression):
        return re.match(WhileLoop.prefix, expression) is not None

    def is_first_pass(self):
        return self.in_inspection

    def end_while_inspection(self):
        self.in_inspection = False

    def add_line(self, line):
        self.lines.append(line)

    def get_lines(self):
        return self.lines
    
    def get_condition(self) -> Expression:
        return self.condition