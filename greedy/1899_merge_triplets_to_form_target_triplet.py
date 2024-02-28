from typing import List 

def merge_triplets(triplets: List[List[int]], target: List[int]) -> bool:
    found = set()

    for triplet in triplets:
        if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
            continue
        
        for index, value in enumerate(triplet):
            if value == target[index]:
                found.add(index)
        
    return len(found) == 3

if __name__ == "__main__":
    print(merge_triplets(triplets=[[2,5,3],[1,8,4],[1,7,5]], target=[2,7,5]))
    print(merge_triplets(triplets=[[3,4,5],[4,5,6]], target=[3,2,5]))
    print(merge_triplets(triplets=[[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target=[5,5,5]))
    print(merge_triplets(triplets=[[15,2,14],[11,5,14],[11,9,10],[4,3,6],[13,3,9],[13,15,9],[15,1,10],[6,8,1],[2,15,6],[15,14,13]], target=[15,3,14]))
    print(merge_triplets([[15,9,8],[2,4,4],[2,6,1],[10,9,4],[10,4,1],[2,12,11],[1,4,2],[15,1,14],[6,2,9],[4,5,11]], target=[10,9,9]))