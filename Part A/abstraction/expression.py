from abc import ABC, abstractmethod

class Expression:
    @abstractmethod
    def evaluate(self):
        pass

class BinaryExpression(Expression):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    @abstractmethod
    def split(expression):
        pass
