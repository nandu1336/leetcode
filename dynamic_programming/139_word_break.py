from typing import List

def word_break(s: str, word_dict: List[str]) -> bool:

    def dfs(target=s, memo={}):
        if not target: return True
        if target in memo: return memo[target]

        for word in word_dict:
            if target.startswith(word):
                target = target[len(word):]
                memo[target] = dfs(target, memo)
                
                if memo[target]:
                    return memo[target]

        return False
    return dfs()

if __name__ == "__main__":
    print(word_break(s="leetcode", word_dict=["leet", "code"]))