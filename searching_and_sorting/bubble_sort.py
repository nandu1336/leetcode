def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
        
    return nums

if __name__ == "__main__":
    print(bubble_sort([7, 12, 9, 11, 3]))
    print(bubble_sort([3, 7, 6, -10, 15, 23.5, 55, -13]))
    print(bubble_sort([11, 9, 14, 7, 13]))
    print(bubble_sort([64, 34, 25, 12, 22, 11, 90, 5]))
    print(bubble_sort([9, 5, 0, 22, 7]))