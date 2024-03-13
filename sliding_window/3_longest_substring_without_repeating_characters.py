def length_of_longest_substring(s: str) -> int:
    visited =set()
    maxlen = 0

    i, j = 0, 0
    while i <= j and j < len(s):
        while j < len(s) and s[j] not in visited:
            visited.add(s[j])
            length = j - i + 1
            maxlen = maxlen if maxlen > length else length
            j += 1

        while j < len(s) and s[j] in visited:
            visited.remove(s[i])
            i += 1
    return maxlen

def length_of_longest_substring_2(s: str) -> int:
    visited = set()
    l = 0
    maxlen = 0

    for r in range(len(s)):
        while s[r] in visited:
            visited.remove(s[l])
            l += 1
        
        visited.add(s[r])
        length = r - l + 1
        maxlen = maxlen if maxlen > length else length
    
    return maxlen

if __name__ == "__main__":
    # print(length_of_longest_substring(s="abcabcbb"))
    print(length_of_longest_substring_2(s="bbbbb"))