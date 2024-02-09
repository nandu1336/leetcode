from typing import List 


def eraseOverlapIntervals(intervals: List[List[int]]) -> int: 
    intervals.sort()
    leftIndex, rightIndex = 0, 1
    popCount = 0
    removedIndices = set()

    left, right = intervals[0], None
    
    for rightIndex in range(1, len(intervals)):
        if rightIndex not in removedIndices:
            
            right = intervals[rightIndex]
            
            if right[0] < left[1]:
                if left[1] > right[1]: 
                    removedIndices.add(leftIndex)
                    leftIndex += 1
                    left = intervals[leftIndex]
                else:
                    removedIndices.add(rightIndex)
                popCount += 1

    return popCount

if __name__ == "__main__":
    print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
    print(eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
    print(eraseOverlapIntervals([[1,2],[2,3]]))
    print(eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]))