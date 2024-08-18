def selection_sort(nums):
    next_index = 0
    
    def find_min(start):
        min_index, min_value = 0, nums[start]
        
        for index, num in enumerate(nums[start: ]):
            if num < min_value: 
                min_value, min_index = num, index

        return min_index + start, min_value
    
    for i in range(len(nums)):
        min_index, min_value = find_min(i)
        nums[min_index], nums[next_index] = nums[next_index], min_value
        next_index += 1

    return nums

if __name__ == "__main__":
    print(selection_sort([ 7, 12, 9, 11, 3]))
    print(selection_sort([7, 12, 9, 11, 3]))
    print(selection_sort([3, 7, 6, -10, 15, 23.5, 55, -13]))
    print(selection_sort([11, 9, 14, 7, 13]))
    print(selection_sort([64, 34, 25, 12, 22, 11, 90, 5]))
    print(selection_sort([9, 5, 0, 22, 7]))