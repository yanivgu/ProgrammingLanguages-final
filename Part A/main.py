import sys
from interpreter import *

def execute_line(line, line_number):
    if line.strip() != "exit()":
        try:
            result = interpret(line, line_number)
            if result is not None:
                result.evaluate()
            return 1
        except ValueError as e:
            print(e, line_number)
            return -1
    return 0

def run_as_console():
    line = ""
    return_code = 1
    line_number = 1
    while (return_code != 0):
        line = input(">>> ")
        return_code = execute_line(line, line_number)
        line_number += 1

if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] == "--console" or sys.argv[1] == "-c":
        run_as_console()
    elif sys.argv[1] == "--file" or sys.argv[1] == "-f":
        if len(sys.argv) != 3:
            print("Usage: python main.py --file <filename>")
        else:
            try:
                with open(sys.argv[2], "r") as f:
                    code = f.readlines()
                    f.close()
                    line_number = 1
                    for line in code:
                        return_code = execute_line(line, line_number)
                        if return_code <= 0:
                            break
                        line_number += 1
            except FileNotFoundError:
                print("File not found")




