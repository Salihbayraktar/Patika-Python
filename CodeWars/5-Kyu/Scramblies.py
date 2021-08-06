def letterCounter(s):
    letterCounter = {}
    for i in s:
        if i not in letterCounter:
            letterCounter[i] = 1
        else:
            letterCounter[i] += 1
    return letterCounter


def scramble(s1, s2):
    s1LetterCounter = letterCounter(s1)
    s2LetterCounter = letterCounter(s2)

    for k, v in s1LetterCounter.items():
        try:
            if k in s2LetterCounter:
                s2LetterCounter[k] -= v
            if s2LetterCounter[k] <= 0:
                del s2LetterCounter[k]
        except:
            pass
    return True if len(s2LetterCounter) == 0 else False

s1 = 'sfalidfgsdfsdfdfsgdsghghdfgbayrhfdfahdfsgkfgjdfsjdftar'
s2 = 'salihbayraktar'
print(scramble(s1, s2))



