def unique_in_order(iterable):
    if len(iterable) == 0:
        return []

    resultList = [iterable[0]]
    for i in range(1, len(iterable)):
        if iterable[i - 1] != iterable[i]:
            resultList.append(iterable[i])
    return resultList
