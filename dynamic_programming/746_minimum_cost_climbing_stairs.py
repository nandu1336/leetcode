from typing import List 

def min_cost_climbing_stairs(cost: List[int]) -> int:
    N = len(cost)

    def dfs(i, cache={}):
        if i in cache: return cache[i]
        if i >= N: return 0

        one, two = dfs(i + 1), dfs(i + 2)
        if one > two: 
            one = two

        res = cost[i] + one
        cache[i] = res
        return res
    
    one = dfs(0)
    two = dfs(1)
    return one if one < two else two

if __name__ == "__main__":
    print(min_cost_climbing_stairs(cost=[10, 15, 20]))
    print(min_cost_climbing_stairs(cost=[1,100,1,1,1,100,1,1,100,1]))