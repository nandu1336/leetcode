from typing import List 

def subsets(nums: List[int]) -> List[List[int]]:
    res = [[]]
    N = len(nums)
    def dfs(i, cur=[]):
        cur.append(nums[i])
        res.append(cur[:])

        for j in range(i+1, N):
            dfs(j, cur)
        
        cur.pop()

    for i in range(N):
        dfs(i)
    return res


if __name__ == "__main__":
    print(subsets(nums=[1, 2, 3]))