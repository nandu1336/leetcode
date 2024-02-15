from typing import List

def jump_game(stairs: List[int]) -> bool:
    last_index = len(stairs) - 1
    next_closest_truth = last_index
    
    for i in range(last_index, -1, -1):
        if i + stairs[i] >= next_closest_truth:
            next_closest_truth = i
    
    return next_closest_truth == 0


if __name__ == "__main__":
    print(jump_game([2,3,1,1,4]))
    print(jump_game([2,0,0]))