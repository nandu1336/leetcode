from typing import List 

def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    ROWS, COLUMNS = len(image), len(image[0])
    colored = set()
    source_color = image[sr][sc]
    def dfs(r, c):
        if r >= ROWS or c >= COLUMNS or r < 0 or c < 0 or (r, c) in colored or image[r][c] != source_color:
            return 

        colored.add((r, c))
        image[r][c] = color

        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    dfs(sr, sc)
    return image


def flood_fill2(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    ROWS, COLUMNS = len(image), len(image[0])
    colored = set()
    source_color = image[sr][sc]
    queue = [(sr, sc)]
    
    while queue:
        x, y = queue.pop()
        if x < 0 or x >= ROWS or y < 0 or y >= COLUMNS or (x, y) in colored or image[x][y] != source_color:
                continue
    
        colored.add((x, y))
        image[x][y] = color

        for node in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
            queue.append(node)

    return image

if __name__ == "__main__":
    
    print(flood_fill2(image=[[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, color=2))
    print(flood_fill2(image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, color=0))
