from typing import List

def insert_interval(intervals: List[int], newInterval: List[int]):
    res = []

    for index, interval in enumerate(intervals):
        if newInterval[0] <= interval[1] and newInterval[1] >= interval[0]: 
            newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        
        elif newInterval[0] > interval[1]: 
            res.append(interval)
        
        elif newInterval[1] < interval[0]:
            res.append(newInterval) 
            res += intervals[index:]
            return res
    
    res.append(newInterval)
    return res


if __name__ == "__main__":
    print(insert_interval(intervals=[[1,3],[6,9]], newInterval=[2,5]))
    print(insert_interval(intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval=[4,8]))
    print(insert_interval(intervals=[[2,5],[6,7],[8,9]], newInterval=[0,1]))