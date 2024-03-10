from typing import List

def num_islands(grid: List[List[int]]) -> int:
    ROWS = len(grid)
    COLUMNS = len(grid[0])
    visited = set()
    count = 0

    def bfs(i, j):
        if i < 0 or i >= ROWS or j < 0 or j >= COLUMNS:
            return False
        
        if grid[i][j] == '1' and (i, j) not in visited:
            visited.add((i, j))
            bfs(i+1, j)
            bfs(i, j+1)
            bfs(i, j-1)
            bfs(i-1, j)
            
            return True

    for i in range(ROWS):
        for j in range(COLUMNS):
            if bfs(i, j):
                count += 1

    return count 

if __name__ == "__main__":
    # print(num_islands( grid = [
    #         ["1","1","1","1","0"],
    #         ["1","1","0","1","0"],
    #         ["1","1","0","0","0"],
    #         ["0","0","0","0","0"]
    #         ]))

    print(num_islands(grid=[
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
            ]))