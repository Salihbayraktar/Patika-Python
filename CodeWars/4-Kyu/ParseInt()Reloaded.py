def parse_int(string):
    string = string.replace(' and', '')
    string = string.replace('-', ' ')
    numberStrList = string.split(' ')
    stringToAdded = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
                     'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18,
                     'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90, }

    number = 0
    if len(numberStrList) == 1:
        if numberStrList[0] in stringToAdded:
            return stringToAdded[numberStrList[0]]

    resultList = []
    for numberStr in numberStrList:
        if numberStr in stringToAdded:
            number += stringToAdded[numberStr]
        elif numberStr == 'hundred':
            number *= 100
        elif numberStr == 'thousand':
            number *= 1000
            resultList.append(number)
            number = 0
        elif numberStr == 'million':
            number *= 1000000
            resultList.append(number)
            number = 0

    resultList.append(number)
    result = 0
    for i in resultList:
        result += i

    return result
