def count(string):
    countChars = {}
    for i in string:
        if i not in countChars:
            countChars[i] = 1
        else:
            countChars[i] += 1
    return countChars


str = 'asdjbhauıwdshdjasdhuıasdhaıusdww'
print(count(str))
