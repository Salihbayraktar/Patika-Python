import re


def alphanumeric(password):
    if len(password) == 0: return False
    return False if re.search('[^\w\d]|[_]', password) else True


password = 'hello world_'
print(alphanumeric(password))
"""
import re


def alphanumeric(password):
    if len(password) == 0:
        return False
    if re.search('[^\w\d]|[_]', password):
        return False
    else:
        return True
"""
