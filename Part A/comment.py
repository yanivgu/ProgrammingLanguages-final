import re

comment_prefix = r"#"

def remove_comments(code):
    return re.sub(comment_prefix + ".*", "", code)