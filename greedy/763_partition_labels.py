from typing import List

def partitionLabels(s: str) -> List[int]:
    last_index_map = {}
    for index, char in enumerate(s):
        last_index_map[char] = index

    res = []
    i = 0
    while i < len(s):
        right = last_index_map[s[i]]
        
        j = i
        while j < right:
            last = last_index_map[s[j]]
            if last > right:
                right = last
            j += 1
        
        res.append(j - i + 1)
        i = j + 1
    return res
        
if __name__ == "__main__":
    print(partitionLabels(s="ababcbacadefegdehijhklij"))
    print(partitionLabels(s="caedbdedda"))