def namelist(names):
    print(names)
    result = ''
    for i in range(len(names)):
        if i < len(names) - 2:
            result += names[i]['name'] + ', '
        elif i < len(names) - 1:
            result += names[i]['name'] + ' & '
        else:
            result += names[i]['name']
    return result


names = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]
print(namelist(names))
