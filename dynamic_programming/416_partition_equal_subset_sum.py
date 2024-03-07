from typing import List 

def can_partition(nums: List[int]) -> bool:
    numsum = sum(nums)
    if numsum % 2 != 0: return False 
    find = numsum // 2
    resset = set()
    resset.add(0)

    for num in nums:
        tempset = set(resset)

        for entry in resset:
            tempset.add(num+entry)

        resset = tempset

    return find in resset
if __name__ == "__main__":
    print(can_partition(nums=[1, 5, 11, 5]))