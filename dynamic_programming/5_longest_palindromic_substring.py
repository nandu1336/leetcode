def longest_palindrome(s: str) -> str:
    res = ""
    max_len = 0
    N = len(s)

    def find_longest_palindrome(start, end):

        while start >= 0 and end < N and s[start] == s[end]:
            start -= 1
            end += 1
        
        start += 1
        end -= 1

        return end - start + 1, s[start: end+1]
    
    for i in range(len(s)):
        odd_length, odd_palindrome = find_longest_palindrome(i, i)
        if odd_length > max_len:
            res = odd_palindrome
            max_len = odd_length
    
        even_length, even_palindrome = find_longest_palindrome(i, i+1)
        if even_length > max_len:
            res = even_palindrome
            max_len = even_length

    return res

if __name__ == "__main__":
    print(longest_palindrome(s="babad"))
    print(longest_palindrome(s="cbbd"))
    print(longest_palindrome(s="aacabdkacaa"))
    print(longest_palindrome(s="tattarrattat"))