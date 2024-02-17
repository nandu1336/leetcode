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

if __name__ == "__main__":
    print(min_jumps([2,3,1,1,4]))
    print(min_jumps([1, 2, 3]))