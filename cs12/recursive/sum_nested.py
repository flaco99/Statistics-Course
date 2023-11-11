def sum_nested(nlist):
    'sumes the numbers in a nested list of numbers'
    acc = 0
    for item in nlist:
        if isinstance(item, int):
            acc += item
        else:
            acc += sum_nested(item)
    return acc

sample_list = [1,[2,3],[4,[5,6]],0]
print(sum_nested(sample_list))