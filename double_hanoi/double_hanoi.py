
def solution(list_of_disks, leftIncreasingValues, rightDecreasingValues):
    left = [leftIncreasingValues]
    right = [rightDecreasingValues]
    for disk in list_of_disks:
        original_left = len(left)
        evaluate_info(disk, left)
        if original_left == len(left):
            evaluate_info(disk, right, False)
    return len(left) + len(right) - 2

def evaluate_info(disk, aList, isLower=True):
    if disk not in aList:
        if should_evaluated(aList, disk, isLower):
            analyse_data(disk, aList, isLower)
    return aList

def should_evaluated(aList, disk, isLower=True):
    evaluation_field = max(aList) if isLower else min(aList)
    return disk < evaluation_field if isLower else disk > evaluation_field

def analyse_data(disk, aList, isLower=True):
    for idx, val in enumerate(aList):
        next_idx = idx + 1
        next_val = obtain_next_val(disk, aList, next_idx, isLower)
        if isLower:
            evaluate_and_add(disk, idx, aList, next_val, val)
        evaluate_and_add(disk, idx, aList, val, next_val)

def obtain_next_val(disk, aList, next_idx, isLower=True):
    default = (disk - 1) if isLower else (disk + 1)
    return aList[next_idx] if next_idx < len(aList) else default

def evaluate_and_add(disk, idx, aList, maximum_val, minimum_val):
    if minimum_val > disk > maximum_val:
        aList.insert(idx + 1, disk)












