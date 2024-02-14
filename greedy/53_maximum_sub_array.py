from typing import List 


def maximum_sub_array(nums: List[int]) -> int:
    max_sum_array = [0] * len(nums)
    max_sum_array[-1] = nums[-1]

    for i in range(len(nums) - 2, -1, -1):
        max_sum_array[i] = max(nums[i], nums[i] + max_sum_array[i+1])

    return max(max_sum_array)
    
    """
        below code looks little better than the above but performed badly compared 
        to the above code. The reason for this could be that fact that I am calling 
        max operator twice on each iteration, which apparently seems to take more time 
        than find max of the whole list once at the end as done in the above code.
    """
    max_sum, next_max_sum = nums[-1], nums[-1]

    for i in range(len(nums) - 2, -1, -1):
        next_max_sum = max(nums[i], nums[i] + next_max_sum)
        max_sum = max(max_sum, next_max_sum)
    return max_sum
    


if __name__ == "__main__":
    print(maximum_sub_array(nums=[-2,1,-3,4,-1,2,1,-5,4]))