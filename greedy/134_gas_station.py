from typing import List

def can_complete_cicuit(gas: List[int], cost: List[int]) -> bool:
    '''
    Note: 
    
    1. I did not understand why when we can't reach a station B from station A, you can't reach
    anyother station that is b/w A and B (inclusive A, exclusing B).
    
    2. I also did not understand why when you reach the end of the list, you don't have to try 
    with stations start at 0 again.
    '''
    if sum(gas) < sum(cost): return -1
    
    res = 0
    balance_gas = 0

    for i in range(len(gas) - 1):
        balance_gas += gas[i] - cost[i]

        if balance_gas < 0:
            balance_gas = 0
            res = i + 1
    return res
    

if __name__ == "__main__":
    print(can_complete_cicuit(gas=[1,2,3,4,5], cost=[3,4,5,1,2]))
    print(can_complete_cicuit(gas=[2,3,4], cost=[3,4,3]))
    print(can_complete_cicuit(gas=[5,1,2,3,4], cost=[4,4,1,5,1]))
    print(can_complete_cicuit(gas=[4,5,3,1,4], cost=[5,4,3,4,2]))
    print(can_complete_cicuit(gas=[3,1,1], cost=[1,2,2]))