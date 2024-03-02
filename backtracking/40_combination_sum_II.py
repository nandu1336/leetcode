from typing import List 

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    N = len(candidates)
    candidates.sort()

    def dfs(i=0, combo=[], req=0):
        if req == target:
            res.append(combo[:])
            return 

        if i == N or req > target:
            return 
        
        combo.append(candidates[i])
        dfs(i + 1, combo, req + candidates[i])
        combo.pop()

        while i + 1 < N and candidates[i+1] == candidates[i]:
            i += 1
        dfs(i+1, combo, req)

    dfs()
    return res

def combination_sum_2(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    res = []
    N = len(candidates)

    def dfs(i=0, rem=target, combo=[]):
        if rem == 0:
            res.append(combo[:])
            return 
        
        for j in range(i, N):
            
            if j > i and candidates[j] == candidates[j-1]: continue
            if candidates[j] > rem: return 
        
            dfs(j+1, rem - candidates[j], combo + candidates[j: j+1])
    dfs()
    return res

if __name__ == "__main__":
    print(combination_sum_2(candidates=[10,1,2,7,6,1,5], target=8))