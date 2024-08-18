def partition(array, start, end):
    pivot_index, pivot_value = end-1, array[end-1]

    for i in range(start, end):
        value = array[i]

        if (i <= pivot_index and value > pivot_value) or (i > pivot_index and value < pivot_value):
            array[pivot_index], array[i], pivot_index = value, pivot_value, i 

    return pivot_index

def quick_sort(nums, start=0, end=None):
    if end is None: 
        end = len(nums)
    
    if start < end:
        pivot_index = partition(nums, start, end)
        quick_sort(nums, start, pivot_index)
        quick_sort(nums, pivot_index+1, end)

    return nums

if __name__ == "__main__":
    print(quick_sort([11, 9, 14, 7, 13]))
    print(quick_sort([64, 34, 25, 12, 22, 11, 90, 5]))
    print(quick_sort([9, 5, 0, 22, 7]))
    
