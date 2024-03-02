from typing import List 

def combination_sum(candidates: List[int], sum: int) -> List[List[int]]:
    res = []
    N = len(candidates)

    def dfs(index, temp_sum, combo):
        if temp_sum > sum: return 

        if temp_sum == sum: 
            res.append(combo[:])
            return 
        
        for j in range(index, N):
            num = candidates[j]
            
            combo.append(num)
            dfs(j, temp_sum+num, combo)
            combo.pop()

    
    dfs(0, 0, [])

    return res
if __name__ == "__main__":
    print(combination_sum(candidates=[2, 3, 6, 7], sum=7))