def insertion_sort(nums):
    n = len(nums)

    for i in range(1, n):
        value = nums[i]
        insert_index = i 

        for j in range(i-1, -1, -1):
            if value < nums[j]:
                nums[j+1] = nums[j]
                insert_index = j 

            else:
                break
            
        nums[insert_index] = value 
    return nums

if __name__ == "__main__":
    print(insertion_sort([11, 9, 14, 7, 13]))
    print(insertion_sort([64, 34, 25, 12, 22, 11, 90, 5]))
    print(insertion_sort([9, 5, 0, 22, 7]))