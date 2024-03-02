from typing import List 

def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = [[]]
    visited = set() 
    N = len(nums)

    def dfs(i, combo=[]):
        combo.append(nums[i])
        combo_tuple = tuple(combo)
        if combo_tuple not in visited:
            visited.add(combo_tuple)
            res.append(combo[:])
        
        for j in range(i+1, N):
            dfs(j, combo)

        combo.pop()
    
    for i in range(N):
        dfs(i)
    return res

def subsets_with_dup2(nums: List[int]) -> List[List[int]]:
    '''
        This is not very intuitive to me but seems to work better than my code.
        Copied this from neetcode.
    '''
    res = []
    nums.sort()

    def backtrack(i, subset):
        if i == len(nums):
            res.append(subset[:])
            return 

        subset.append(nums[i])
        backtrack(i+1, subset)

        subset.pop()
        
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        backtrack(i+1, subset)

    backtrack(0, [])    
    return res


if __name__ == "__main__":
    print(subsets_with_dup2(nums=[1, 2, 2]))
    print(subsets_with_dup2(nums=[4, 1, 4]))