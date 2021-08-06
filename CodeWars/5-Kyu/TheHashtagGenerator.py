def generate_hashtag(s):
    if len(s) == 0:
        return False

    wordList = s.split(' ')
    for i in range(len(wordList)):
        wordList[i] = wordList[i].lower().capitalize()

    result = '#' + ''.join(wordList)

    return result if len(result) <= 140 else False


strin2 = 'CoDeWars Is NiCe'
print(generate_hashtag(strin2))