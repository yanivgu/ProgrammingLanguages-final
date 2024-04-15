from interpreter import *

code = ""
while (code.strip() != "exit"):
    code = input(">>> ")
    if code != "exit":
        try:
            result = interpret(code)
            result.evaluate()
        except ValueError as e:
            print(e)
