input_list = [7, 3, 8, 5, 1, 0, 3, 6, 3, 9, 3, 5]


def select_sort(nums):  # time complexity = O(n**2)
    nums_len = len(nums)
    for i in range(nums_len):
        unsorted_section = nums[i:]
        lowest_num = min(nums[i:])  # time complexity of min() = O(n)
        lowest_index = unsorted_section.index(lowest_num)+i
        current_num = nums[i]
        nums[i] = lowest_num
        nums[lowest_index] = current_num
    return nums


print(select_sort(input_list))