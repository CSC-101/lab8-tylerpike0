import math


#Task 1

def groups_of_3(nums: list[int]) -> list[list[int]]:
    should_continue = True
    num_length = len(nums)
    sublists = []
    index = 0
    while should_continue:
        sublist = []
        for i in range(3):
            if num_length > index:
                sublist.append(nums[index])
                index += 1
            else:
                should_continue = False
        if sublist:
            sublists.append(sublist)
    return sublists

