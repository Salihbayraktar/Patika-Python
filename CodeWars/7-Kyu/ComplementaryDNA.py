def DNA_strand(dna):
    dnaList = list(dna)
    print(dnaList)
    for i in range(len(dnaList)):
        if dnaList[i] == 'T':
            dnaList[i] = 'A'
        elif dnaList[i] == 'A':
            dnaList[i] = 'T'
        elif dnaList[i] == 'G':
            dnaList[i] = 'C'
        else:
            dnaList[i] = 'G'
    return ''.join(map(str, dnaList))

print(DNA_strand('AAAA'))