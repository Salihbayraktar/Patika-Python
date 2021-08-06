def alphabet_position(text):
    text = text.lower()
    resultList = []
    for i in text:
        if i.isalpha():
            resultList.append(str(ord(i) - 96))
    return ' '.join(resultList)
