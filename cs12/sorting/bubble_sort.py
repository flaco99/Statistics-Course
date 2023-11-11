input_list = [7, 3, 8, 5, 1, 0, 3, 6, 3, 9, 3, 5]


def bubble_sort(nums):  # time complexity = O(n**2)
    nums_len = len(nums)
    for n in range(nums_len):
        swaps = 0
        for i in range(nums_len-n-1):
            n1 = nums[i]
            n2 = nums[i+1]
            if n1>n2:
                nums[i] = n2
                nums[i+1] = n1
                swaps += 1
        if swaps == 0:
            return nums
    return nums


print(bubble_sort(input_list))