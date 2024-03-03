def climb_stairs(n: int) -> int:
    count = 0

    def dfs(rem=n, cache={}):
        nonlocal count
        
        if rem in cache: 
            return cache[rem]
        
        if rem < 0: return 0
        if rem == 0:
            return 1
        
        val = dfs(rem-1) + dfs(rem-2)
        cache[rem] = val
        return val 

    return dfs()

if __name__ == "__main__":
    print(climb_stairs(n=2))