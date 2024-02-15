from typing import List

def jump_game(nums: List[int]) -> bool:
    last_index = len(nums) - 1
    next_closest_truth = last_index
    
    for index in range(last_index, -1, -1):
        if index + nums[index] >= next_closest_truth:
            next_closest_truth = index
    
    return next_closest_truth == 0

def jump_game_2(nums: List[int]) -> bool:
    max_distance = nums[0]
    
    for index in range(1, len(nums)):
        if max_distance < index: return False
        max_distance = max(max_distance, index + nums[index])

    return max_distance >= len(nums) - 1


if __name__ == "__main__":
    print(jump_game_2([2,3,1,1,4]))
    print(jump_game_2([2,0,0]))