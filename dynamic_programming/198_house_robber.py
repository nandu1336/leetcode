from typing import List 

def rob(nums: List[int]) -> int:
    N = len(nums)

    def dfs(i=0, loot=0, memo={}):
        if i in memo: return memo[i]
        if i == N: return loot
        
        max_loot = 0
        for j in range(i+2, N):
            temp_loot = dfs(j, loot)
            max_loot = temp_loot if temp_loot > max_loot else max_loot
        
        memo[i] = nums[i] + max_loot   
        return memo[i]
    
    return max(dfs(0), dfs(1))

def rob_dp(nums: List[int]) -> int:
    house1, house2 = 0, 0

    for num in nums:
        new_rob = max(house1 + num, house2)
        house1, house2 = house2, new_rob
    
    return house2

if __name__ == "__main__":
    print(rob_dp(nums=[1, 2, 3, 1]))
    print(rob_dp(nums=[2, 7, 9, 3, 1]))