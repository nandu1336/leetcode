from typing import List
'''
    given a number of process N, and their weight times, return the list of no. of process present in the 
    queue after each second.

    after ti second:
    - a new process from queue is processed in FIFO order
    - all those process whose weight time < ti are removed along with the one that is just processed.
'''
def temp(wait_time: List[int]) -> List[int]:
    N = len(wait_time)
    included = set([i for i in range(N)])
    temp = set(included)
    res = [N]

    for i in range(N):
        if i in included:
            included.remove(i)
            temp.remove(i)

            for j in included:
                if wait_time[j] - 1 == 0:
                    temp.remove(j)
                    continue
                wait_time[j] -= 1


            included = set(temp)
            res.append(len(included))
    return res

if __name__ == "__main__":
    print(temp(wait_time=[3, 1, 2, 1]))