from typing import List 

def generate_parenthesis(n: int) -> List[str]:
    res = []
    stack = []

    def backtrack(oc, cc):
        if oc == cc == n:
            res.append("".join(stack))
        
        if oc < n:
            stack.append("(")
            backtrack(oc+1, cc)
            stack.pop()
        
        if cc < oc and cc < n:
            stack.append(")")
            backtrack(oc, cc+1)
            stack.pop()

    backtrack(0, 0)
    return res



if __name__ == "__main__":
    print(generate_parenthesis(n=3))