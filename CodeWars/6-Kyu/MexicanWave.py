def wave(people):
    if len(people) == 0:
        return people
    resultList = []
    for i in range(len(people)):
        if people[i] != ' ':
            waveStr = people[:i] + str.upper(people[i]) + people[i+1:]
            resultList.append(waveStr)
    return resultList

people = 'two words'
print(wave(people))