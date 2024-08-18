def merge(a, b):
    aindex = bindex = 0
    res = []

    while aindex < len(a) and bindex < len(b):
        if a[aindex] < b[bindex]:
            res.append(a[aindex])
            aindex += 1
        else:
            res.append(b[bindex])
            bindex += 1
    
    res.extend(a[aindex: ])
    res.extend(b[bindex: ])
    
    return res

def merge_sort(nums):
    if len(nums) <= 1: return nums 

    mid = len(nums) // 2

    left_sub_list =  merge_sort(nums[: mid])
    right_sub_list = merge_sort(nums[mid: ])

    return merge(left_sub_list, right_sub_list)

if __name__ == "__main__":
    print(merge_sort([3, 7, 6, -10, 15, 23.5, 55, -13]))
    print(merge_sort([11, 9, 14, 7, 13]))
    print(merge_sort([64, 34, 25, 12, 22, 11, 90, 5]))
    print(merge_sort([9, 5, 0, 22, 7]))