# Part 1 + 2
## Design decisions
### Variables
- Variable length is up to 20 charachters
- Variables must begin in a letter (upper or lower case)

### Operations
The language supports the following arithmetic operations
- Addition - Adds two integers - `add`
- Substraction - Substracts one integer from the other - `sub`
- Multiplication - Multiplies two integers - `mul`
- Division - Divides one integer by the other - `div`

In addition the language supports the following operations
- `print` - prints a number, or the value of a variable into the console.

### Syntax
For simplicity and common use, the syntax of the language is:
- Single line commands - the commands and all the arguments for it must fit on the same line
- Single command on each line - there cannot be multiple commands on a single line of code
- Each command is structured as follows: first the command name, followed by a space, and then the arguments for the command separated by spaces
- Commands, variables, operators and numbers must be split with space for simplicity and visibility
```
print 3
print variable3
add 231 123
```
### Data types
The language supports only integer data type

### Control flows
- Sequential Execution - Statements are executed in the order they appear in the code, from top to bottom.

## BNF