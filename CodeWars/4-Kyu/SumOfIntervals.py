def sum_of_intervals(intervals):
    counter = 0
    number = set()
    for i in range(len(intervals)):
        for j in range(intervals[i][0],intervals[i][1]):
            if j not in number:
                number.add(j)
                counter += 1
    return counter


print(sum_of_intervals([(-464, 460), (-271, 124), (328, 395), (217, 228)]))
