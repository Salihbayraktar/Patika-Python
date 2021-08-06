def strings_in_max_depth(s):
    if '(' not in s:
        result = []
        result.append(s)
        return result

    deepestBracelestCounter = 0
    braceletCounter = 0
    for i in s:
        if i == '(':
            braceletCounter += 1
        elif i == ')':
            braceletCounter -= 1
        if braceletCounter > deepestBracelestCounter:
            deepestBracelestCounter = braceletCounter

    braceletCounter = 0
    result = []
    deepestBraceletStr = ''
    for i in s:
        if braceletCounter == deepestBracelestCounter:
            deepestBraceletStr += i
        if i == '(':
            braceletCounter += 1
        elif i == ')':
            deepestBraceletStr = deepestBraceletStr[0:len(deepestBraceletStr) - 1]
            if braceletCounter == deepestBracelestCounter:
                result.append(deepestBraceletStr)
            deepestBraceletStr = ''
            braceletCounter -= 1

    return result
