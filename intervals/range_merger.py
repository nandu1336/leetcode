from typing import List 

class RangeMerger:
    def __init__(self) -> None:
        self.ranges: List[int] = []
        
    def insert(self, new_range: List[int]) -> None:
        if not self.ranges: 
            self.ranges.append(new_range)
            return self.ranges
        
        index = 0
        temp_ranges = []

        while index < len(self.ranges):

            range = self.ranges[index]
            if self.has_overlap(range, new_range):
                new_range = self.merge(range, new_range)
                
            elif new_range[1] < range[0]:
                temp_ranges = [new_range] + self.ranges[index: ]
                break
            
            elif new_range[0] > range[1]: 
                temp_ranges = self.ranges[:index + 1] + [new_range]
                break

            index += 1

        self.ranges = temp_ranges if temp_ranges else [new_range]

        return self.ranges
        

    def query(self, num: int) -> bool:
        for start, end in self.ranges:
            if num >= start and num <= end: return True
        return False

    def has_overlap(self, existing_range: List[int], new_range: List[int]):
        return new_range[0] <= existing_range[1] and new_range[1] >= existing_range[0]
    
    def merge(self, existing_range, new_range):
        return [min(existing_range[0], new_range[0]), max(existing_range[1], new_range[1])]
    

if __name__ == "__main__":
    merger = RangeMerger()
    print(merger.insert([4, 5]))
    print(merger.insert([2, 3]))
    print(merger.insert([2, 4]))
    print(merger.insert([1, 8]))
    print(merger.insert([20, 25]))
    print(merger.insert([8, 21]))
    print(merger.insert([-4, 0]))

    print(merger.query(1))
    print(merger.query(11))
    print(merger.query(111))
    print(merger.query(21))