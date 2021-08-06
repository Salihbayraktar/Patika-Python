def play_pass(s, n):
    n = n % 26
    resultList = []
    for i in range(len(s)):
        if ord('A') <= ord(s[i]) <= ord('Z'):
            letterByte = ord(s[i]) + n
            if letterByte > ord('Z'):
                letterByte -= 26
            if i % 2 == 1:
                resultList.append(chr(letterByte).lower())
            else:
                resultList.append(chr(letterByte).upper())
        elif s[i].isdigit():
            resultList.append(str(9 - int(s[i])))
        else:
            resultList.append(s[i])
    return ''.join(resultList)[::-1]
