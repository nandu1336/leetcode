from typing import List

def min_jumps(nums: List[int]) -> int:
    step_count = len(nums)
    min_jumps_needed = [step_count] * step_count
    min_jumps_needed[-1] = 0
    
    for index in range(step_count - 2, -1, -1):
        possible_dest = index + nums[index]
        if possible_dest >= step_count - 1:
            min_jumps_needed[index] = 1

        else:
            min_jumps_needed[index] = 1 + min(min_jumps_needed[index: possible_dest + 1])
    return min_jumps_needed[0]

def min_jumps_2(nums: List[int]) -> int:

    l, r = 0, 0
    res = 0

    while r < len(nums) - 1:
        farthest = 0
        for i in range(l, r + 1):
            temp = i + nums[i]
            farthest = farthest if farthest > temp else temp
        
        res += 1
        l, r = r + 1, farthest
    return res

if __name__ == "__main__":
    print(min_jumps_2([2,3,1,1,4]))
    print(min_jumps_2([1, 2, 3]))