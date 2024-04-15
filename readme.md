# Part 1 + 2
## Design decisions
### Variables
- Variable length is up to 20 charachters
- Variables must begin in a letter (upper or lower case)

### Operations
The language supports the following arithmetic operations
- Addition - Adds two integers - `<expression> + <expression>`
- Substraction - Substracts one integer from the other - `<expression> - <expression>`
- Multiplication - Multiplies two integers - `<expression> * <expression>`
- Division - Divides one integer by the other - `<expression> / <expression>`
- Assignment - Set the value of a variable to the result of an expression - `<variable> = <expression>`

In addition the language supports the following commands
- `print(<expression>)` - prints the result of the provided expression to the console. If a variable is provided in the expresion, print it's current value.
- `print_scope_variables()` - prints the defined variables in the program

### Syntax
- Single line commands - the commands and all the arguments for it must fit on the same line
- Support multiple mathematical operations on a single line
- Chain assignment - support assigning multiple variables at once
- Comments are begin with `#` - any suffix is disregarded
```
print(3)
my_var = 3 + 2 * 5
print(my_var)
my_var = 12 # this is a very useful comment
```
### Data types
The language supports only integer data type

### Control flows
- Sequential Execution - Statements are executed in the order they appear in the code, from top to bottom.

## BNF
```
<assignment>      ::= <assignment> "=" <set_statement> | <identifier>=<expression>
<print_statement> ::= "print("<expression>")"
<expression>      ::= <expression> <operator> <expression> | <expression> <operator> <basic_expression> | <basic_expression> <operator> <expression> | <basic_expression> <operator> <basic_expression>
<operator>        ::= "+" | "-" | "*" | "/"
<basic_expression>::= <identifier> | <number>
<number>          ::= [0-9]+
<identifier>      ::= [a-zA-Z][a-zA-Z0-9]*
```