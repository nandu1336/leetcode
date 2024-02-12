from typing import List 
import heapq as hq


def minInterval(intervals: List[List[int]], queries: List[int]) -> List[int]:
    intervals.sort()
    minHeap = []
    index = 0
    res = {}

    for query in sorted(queries):
        
        while index < len(intervals) and intervals[index][0] <= query:
            start, end = intervals[index][0], intervals[index][1]
            hq.heappush(minHeap, (end - start + 1, end))
            index += 1

        while minHeap and minHeap[0][1] < query:
            hq.heappop(minHeap)

        res[query] = minHeap[0][0] if minHeap else -1

    return [res[query] for query in queries]
        
if __name__ == "__main__":
    print(minInterval(intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]))
    print(minInterval(intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]))