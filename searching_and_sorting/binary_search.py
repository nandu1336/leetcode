def binary_serach(sorted_list, target):
    
    def inner(start=0, end=None):
        nonlocal sorted_list, target
        
        if end is None:
            end = len(sorted_list)

        if start >= end: return -1
        mid = (start + end) // 2
        value = sorted_list[mid]
        if value == target:
            return mid
        
        if target < value:
            return inner(start, mid-1)

        return inner(mid+1, end)

    return inner()

if __name__ == "__main__":
    print(binary_serach([5, 11, 12, 22, 25, 34, 64, 90], target=614))