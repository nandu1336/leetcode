from typing import List 


def merge_intervals(intervals: List[int]):
    intervals.sort()
    res = []
    left, right = intervals[0], None
    
    for i in range(1, len(intervals)):
        right = intervals[i]

        if left[1] >= right[0] and left[0] <= right[1]: 
            left = [min(left[0], right[0]), max(left[1], right[1])]
            right = None
            
        else :
            res.append(left)
            left = right
            
    res.append(right) if right else res.append(left)
    return res

        

if __name__ == "__main__":
    print(merge_intervals(intervals=[[1,3],[2,6],[8,10],[15,18]]))
    print(merge_intervals([[1, 4], [0, 0]]))
    print(merge_intervals([[0, 2]]))