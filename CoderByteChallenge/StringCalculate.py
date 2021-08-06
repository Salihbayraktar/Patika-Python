def StringCalculate(strParam):
    # code goes here
    operators = '+-*/'
    strList = []
    for i in range(len(strParam)-1):
        if strParam[i] == ')' and strParam[i+1] not in operators and strParam[i+1] != ')' :
            strList.append(strParam[i])
            strList.append('*')
        elif i>0 and strParam[i] == '(' and strList[-1] not in operators and strParam[i-1] != '(':
            strList.append('*')
            strList.append(strParam[i])
        else:
            strList.append(strParam[i])
    strList.append(strParam[-1])
    strParam = ''.join(strList)
    return int(eval(strParam))


# keep this function call here
print(StringCalculate(input()))