from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    res = []
    visited = set()
    N = len(nums)

    def dfs(combo=[]):
        if len(combo) == len(nums):
            res.append(combo[:])
            return 
        
        for num in nums:
            if num not in visited:
                visited.add(num)
                combo.append(num)
                dfs(combo)
                combo.pop()
                visited.remove(num)
    dfs()
    return res

if __name__ == "__main__":
    print(permute(nums=[1, 2, 3]))