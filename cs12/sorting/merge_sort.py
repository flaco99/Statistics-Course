input_list = [7, 3, 8, 5, 1, 0, 3, 6, 3, 9, 3, 5]


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


print(merge_sort(input_list))