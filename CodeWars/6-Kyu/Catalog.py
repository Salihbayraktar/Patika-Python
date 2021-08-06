import re


def catalog(s, article):
    sList = re.findall("<prod>(.*?)</prod>", s)
    resultList = []
    for i in range(len(sList)):
        currentName = re.findall("<name>(.*?)</name>", sList[i])[0]
        if article in currentName:
            prx = re.findall("<prx>(.*?)</prx>", sList[i])[0]
            qty = re.findall("<qty>(.*?)</qty>", sList[i])[0]
            result = currentName + ' > prx: $' + prx + ' qty: ' + qty
            resultList.append(result)
            print(result)
    if not resultList:
        return 'Nothing'
    return '\r\n'.join(resultList)
