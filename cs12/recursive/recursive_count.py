def recursive_count(my_list, item):
    if len(my_list) == 0:
        return 0
    elif my_list[0] == item:
        return recursive_count(my_list[1:], item) + 1
    else:  #len(my_list) > 0 and my_list[0] != itme
        return recursive_count(my_list[1:], item)

sample_list = [1,2,3,4,3,2,1]
print(recursive_count(sample_list, 3))