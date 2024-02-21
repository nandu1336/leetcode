from typing import List
from collections import Counter
import heapq

def is_n_straight_hand(hand: List[int], group_size: int) -> bool:
    '''
        Note: It beat only 5% solutions in leetcode and needs lot of optimization. 
        Will continue working on it.
    '''
    if len(hand) % group_size != 0: return False
    
    hand.sort()
    res, grp = [], []
    i = 0
    visited = set()
    last_card = None
    goto_index = None

    while i < len(hand):
        card = hand[i]
        if last_card is None or last_card + 1 == card:
            if i not in visited:
                visited.add(i)
                grp.append(card)
                last_card = card

                if len(grp) == group_size:
                    res.append(grp)
                    i = goto_index if goto_index else i + 1
                    last_card = None
                    grp = []
                    continue
        else:
            goto_index = goto_index or i
        i += 1

    return len(res) * group_size == len(hand)

def is_n_straight_hand_2(hand: List[int], group_size: int) -> bool:
    '''
    Note: This is little better than the above code, it beat 42.35% of submissions.
    '''
    if len(hand) % group_size != 0: return False

    c = Counter(hand)
    hand_set = set(hand)
    res, grp = [], []

    for card in sorted(hand):
        temp = card
        grp = []
        while c[temp] > 0:
            grp.append(temp)
            c[temp] -= 1
            if c[temp] == 0: 
                hand_set.remove(temp)
                del c[temp]
            
            temp += 1
            if len(grp) == group_size:
                res.append(grp)
                grp = []
                break
    
    return len(res) * group_size == len(hand)

def is_n_straight_hand_3(hand: List[int], group_size: int) -> bool: 
    if len(hand) % group_size != 0: return False

    counter = Counter(hand)
    min_heap = list(counter.keys())
    heapq.heapify(min_heap)
    res, grp = [], []

    while min_heap: 
        card = min_heap[0]
        grp = []

        for i in range(group_size):
            next_card = card + i
            
            if counter.get(next_card, 0) == 0: return False

            grp.append(next_card)
            counter[next_card] -= 1

            if counter[next_card] == 0: 
                heapq.heappop(min_heap)

        if len(grp) == group_size:
            res.append(grp)
    
    return len(res) * group_size == len(hand)

if __name__ == "__main__":
    print(is_n_straight_hand_3(hand=[1,2,3,6,2,3,4,7,8], group_size=3))
    print(is_n_straight_hand_3(hand=[1,2,3,4,5,6], group_size=2))
    print(is_n_straight_hand_3(hand=[1,1,2,2,3,3], group_size=3))
    print(is_n_straight_hand_3(hand=[0, 0], group_size=2))
    print(is_n_straight_hand_3(hand=[1,2,3,4,5], group_size=4))
    print(is_n_straight_hand_3(hand=[8,10,12], group_size=3))