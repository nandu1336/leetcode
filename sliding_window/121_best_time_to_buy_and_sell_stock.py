from typing import List

def max_profit(prices: List[int]) -> int: 
    l, r = 0, 1
    max_profit = 0
    while l < r and r < len(prices):
        buy, sell = prices[l], prices[r]
        profit = sell - buy

        if sell > buy: max_profit = max(profit, max_profit)
        else: l = r
        
        r += 1

    return max_profit    

if __name__ == "__main__":
    print(max_profit(prices=[7, 1, 5, 3, 6, 4]))
    print(max_profit(prices=[7, 6, 4, 3, 1]))