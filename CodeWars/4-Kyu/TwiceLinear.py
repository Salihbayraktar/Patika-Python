from queue import PriorityQueue


def dbl_linear(n):
    nextU = PriorityQueue()
    nextU.put(1)
    controlSet = set()
    counter = 0
    while counter != n:
        counter += 1
        u = nextU.get()
        y = (u * 2) + 1
        z = (u * 3) + 1
        if y not in controlSet:
            nextU.put(y)
            controlSet.add(y)
        if z not in controlSet:
            nextU.put(z)
            controlSet.add(z)
    return nextU.get()


print(dbl_linear(12584))  # 12584  -> 214119
"""
from queue import PriorityQueue

def dbl_linear(n):
    nextU = PriorityQueue()
    nextU.put(1)
    values = set()
    values.add(1)
    # y = 2 * x + 1
    # z = 3 * x + 1
    while len(values) < n * 1.25:
        u = nextU.get()
        y = (u * 2) + 1
        z = (u * 3) + 1
        nextU.put(y)
        nextU.put(z)
        values.add(y)
        values.add(z)
    result = list(values) 
    result.sort()
    #print(result)  
    return result[n]
	# your code
"""
