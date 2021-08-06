def valid_parentheses(string):
    #your code here
    if len(string) == 0:
        return True
    braceletCounter = 0
    for i in string:
        if i == '(':
            braceletCounter += 1
        elif i == ')':
            braceletCounter -= 1
            if braceletCounter < 0:
                return False
    return braceletCounter == 0