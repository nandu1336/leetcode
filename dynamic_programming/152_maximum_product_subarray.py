from typing import List 

def max_product(nums: List[int]) -> int:
    N = len(nums)
    max_products = nums[-1]
    min_products = nums[-1]
    res = nums[-1]
    
    for i in range(N - 2, -1, -1):
        num = nums[i]
        vals = [num, num*max_products, num*min_products]
        max_products = max(vals)
        min_products = min(vals)
        res = max(max_products, min_products, res)

    return res

if __name__ == "__main__":
    print(max_product(nums=[2, 3, -2, 4]))
    print(max_product(nums=[-2, 0, 1]))
    print(max_product(nums=[-1, -2, -3]))