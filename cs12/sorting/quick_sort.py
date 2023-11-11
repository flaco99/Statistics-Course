def quick_sort(nums):
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

sample = [1,5,8,7,4,6,9,5,3,0,4,8,7]

print(quick_sort(sample))