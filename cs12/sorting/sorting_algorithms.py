import time
import random


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


def merge(nums1, nums2):  # time complexity: O(n)
    '''merge 2 sorted lists into 1 sorted list'''
    i = 0
    j = 0
    merged = []
    while (i<len(nums1)) and (j<len(nums2)):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    merged += nums1[i:]
    merged += nums2[j:]
    return merged


def merge_sort(nums):  # time complexity: O(n*log2(n))
    if len(nums) <= 1: # base
        return nums
    else:
        middle_index = len(nums)//2
        l1 = merge_sort(nums[:middle_index])
        l2 = merge_sort(nums[middle_index:])
        return merge(l1, l2)


def quick_sort(nums):  # time complexity: O(n*log2(n)) (but if pivots are chosen badly, it can be O(n**2))
    '''sorts list of numbers'''
    if len(nums) <= 1:
        return nums
    else:
        mid = len(nums)//2
        pivot = nums[mid]
        smaller = []
        pivots = []
        larger = []
        for n in nums:
            if n < pivot:
                smaller.append(n)
            elif n > pivot:
                larger.append(n)
            else:
                pivots.append(n)
    return quick_sort(smaller) + pivots + quick_sort(larger)


# benchmark selection sort
def time_sort():
    for size in [100, 500, 5000]:
        nums = list(range(size))
        random.shuffle(nums)
        start = time.perf_counter()
        nums.sort()
        end = time.perf_counter()
        time_taken = end - start
        tims_ms = round(time_taken*1000, 2)
        print('list length: '+str(size))
        print('Time taken to sort with timsort')
        print(str(tims_ms))


time_sort()