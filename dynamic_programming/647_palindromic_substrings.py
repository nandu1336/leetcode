def count_substrings(s: str) -> int:
    N = len(s)
    count = 0

    def count_possible_palindromes(start, end):
        nonlocal count
        while start >= 0 and end < N and s[start] == s[end]:
            start -= 1
            end += 1
            count += 1


    for i in range(N):
        count_possible_palindromes(i, i)
        count_possible_palindromes(i, i + 1)
    
    return count

if __name__ == "__main__":
    print(count_substrings(s="abc"))