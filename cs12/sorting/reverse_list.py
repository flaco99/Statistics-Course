l = [1,2,3,4,5]

def reversel(list):
    if len(list) <= 1:
        return list
    else:
        return [list[-1]] + reversel(list[:-1])

print(reversel(l))