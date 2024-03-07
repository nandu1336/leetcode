from typing import List 

def locate_earliest_month(stock_prices: List[int]) -> int:
    N = len(stock_prices)
    
    left_sum, right_sum = 0, sum(stock_prices)
    left_count = 0
    min_diff = right_sum
    min_index = 0
    
    
    for index, stock_price in enumerate(stock_prices):
        left_count += 1
        
        left_sum += stock_price
        right_sum -= stock_price
        
        left_avg = left_sum // left_count
        right_avg = right_sum // (N - left_count) if N - left_count > 0 else right_sum
        
        temp_min_diff = abs(left_avg - right_avg)

        if temp_min_diff < min_diff:
            min_diff = temp_min_diff
            min_index = index
        
    return min_index + 1


if __name__ == "__main__":
    print(locate_earliest_month(stock_prices=[1, 3, 2, 4, 5]))
    print(locate_earliest_month(stock_prices=[1, 1, 1, 1, 1]))