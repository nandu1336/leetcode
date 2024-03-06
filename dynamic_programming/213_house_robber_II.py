from typing import List

def rob(nums: List[int]) -> int:
    def helper(nums):
        house1, house2 = 0, 0

        for num in nums:
            new_rob = max(house1 + num, house2)
            house1, house2 = house2, new_rob
        
        return house2
    
    return max(nums[0], helper(nums[1: ]), helper(nums[: -1]))

if __name__ == "__main__":
    print(rob(nums=[2, 3, 2]))
    print(rob(nums=[1, 2, 3, 1]))