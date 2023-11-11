with open('random.txt', 'r') as file:
    big_list = file.readlines()
    for line in big_list:
        # prep line
        list_line = line.split(' ')
        for n in range(len(list_line)):
            int_n = int(list_line[n])
            list_line[n] = int_n
        list_size = len(line)
        print(list_size)