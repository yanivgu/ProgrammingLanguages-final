import re

variable_name_pattern = r'^[a-zA-Z][a-zA-Z0-9]{0,19}$'
variable_name_rules = "Variable names must start with a letter and be at most 20 characters long."

def validate_variable_name(variable):
    if not check_if_variable(variable):
        raise ValueError(str.format("Invalid variable name: {}. {}", variable, variable_name_rules))
    
def check_if_variable(variable):
    return bool(re.match(variable_name_pattern, variable))
