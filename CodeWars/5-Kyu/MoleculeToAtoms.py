def parse_molecule(formula):
    print(formula)
    resultList = []
    molecule = ''
    #lowerFound = False
    upperFound = False
    digitFound = False
    symbols = '()[]'
    for i in range(len(formula)):
        #print(formula[i])
        if i == len(formula) - 1:
            if formula[i].isupper():
                print(molecule)
                resultList.append(molecule)
                molecule = formula[i] + '1'
                resultList.append(molecule)
                break
            elif formula[i].isdigit() and not upperFound:
                molecule += formula[i]
                resultList.append(molecule)
                break
            if upperFound and formula[i].islower():
                molecule += formula[i] + '1'
                resultList.append(molecule)
                molecule = ''
            elif upperFound and formula[i].isdigit():
                molecule += formula[i]
                resultList.append(molecule)
                molecule = ''
            elif formula[i].isupper() and not digitFound:
                molecule += formula[i] + '1'
                resultList.append(molecule)
                molecule = ''
            elif not upperFound and formula[i].isupper():
                molecule += formula[i] + '1'
                resultList.append(molecule)
                molecule = ''
            else:
                resultList.append(formula[i])

        elif not upperFound and formula[i].isupper():
            upperFound = True
            molecule += formula[i]
        elif formula[i].islower():
            # lowerFound = True
            molecule += formula[i]
        elif formula[i].isdigit():
            digitFound = True
            molecule += formula[i]
        elif upperFound and (formula[i] in symbols or formula[i].isupper()):
            # Yeni eleman bulma durumu
            if not digitFound:
                molecule += '1'
            resultList.append(molecule)
            molecule = ''
            if formula[i] in symbols:
                resultList.append(formula[i])
                upperFound = False
            digitFound = False
            if formula[i].isupper():
                molecule += formula[i]
        elif not upperFound and digitFound and formula[i] in symbols:
            digitFound = False
            resultList.append(molecule)
            molecule = ''
            resultList.append(formula[i])
        elif not upperFound and formula[i] in symbols:
            resultList.append(formula[i])


    print(''.join(resultList))

parse_molecule("K4[ON(SO3)2]2")
# return {K: 4, O: 14, N: 2, S: 4}


#parse_molecule("Mg(OH)2")


#parse_molecule('H2O')