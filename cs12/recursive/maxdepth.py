def maxdepth(L):
    if isinstance(L, int):
        return 0
    else:
        max = 0
        for item in L:
            cur_max = 1 + maxdepth(item)
            if cur_max > max:
                max = cur_max
        return max


sample_list = [0, [1, 2], [3, [4, 5]], [[6, [7]], 8]]
print('should print 4')
print(maxdepth(sample_list))