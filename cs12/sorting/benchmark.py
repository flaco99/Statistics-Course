# currently, the lists all length 1000. also there is only one line. there should be three. with increasing lengths

from sorting_algorithms import select_sort
from sorting_algorithms import bubble_sort
from sorting_algorithms import merge_sort
from sorting_algorithms import quick_sort
import time

files_dict = {select_sort:'selection.txt', bubble_sort:'bubble.txt',
              merge_sort: 'merge_sort.txt', quick_sort: 'quick_sort.txt'}


def print_row(in_dict, size):
    second_row = '\n' + (str(size)).ljust(6) + '|'
    for k in in_dict.keys():
        str_time = str(in_dict[k]) + ' ms'
        second_row += str_time.ljust(14) + '|'
    break_row = '\n'+'-'*82
    sum_rows = second_row + break_row
    return sum_rows


for sorting_func in files_dict.keys():
    summary_dict_5000 = {}
    summary_dict_500 = {}
    summary_dict_100 = {}
    for input_file in ['random.txt', 'reverse.txt', 'sorted.txt', 'few_unique.txt', 'almost_sorted.txt']:
        with open(input_file, 'r') as in_file:
            big_list = in_file.readlines()
        for line in big_list:
            # prep line
            if type(line) == str:
                list_line = line.split(' ')
                for n in range(len(list_line)):
                    int_n = int(list_line[n])
                    list_line[n] = int_n
            elif type(line) == list:
                list_line = line
            list_size = len(list_line)
            print(input_file + ' ' + str(list_size))
            # sort the list
            start_time = time.perf_counter()
            sorting_func(list_line)
            end_time = time.perf_counter()
            time_taken = end_time - start_time
            time_ms = round(time_taken*1000, 2)
            # record time
            if list_size == 100:
                summary_dict_100[input_file] = time_ms
            elif list_size == 500:
                summary_dict_500[input_file] = time_ms
            else:
                summary_dict_5000[input_file] = time_ms

    out_file_name = files_dict[sorting_func]
    with open(out_file_name, 'w') as out_file:
        out_file.write(out_file_name.strip('.txt') + ' sort')
        out_file.write('\n')
        out_file.write('\n      |random        |reverse       |sorted        |few_unique    |almost_sorted |'
                       + '\n'+'-'*82)
        out_file.write(print_row(summary_dict_100, 100))
        out_file.write(print_row(summary_dict_500, 500))
        out_file.write(print_row(summary_dict_5000, 5000))


#brute force it