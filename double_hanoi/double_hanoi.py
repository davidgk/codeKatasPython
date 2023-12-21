def check_is_lower(disk, left):
    if disk in left:
        return left
    max_val = max(left)
    if disk < max_val:
        for idx, val in enumerate(left):
            next_idx = idx + 1
            next_val = obtain_next_val(disk, left, next_idx)
            if val > disk >= next_val:
                left.insert(idx+1, disk)
    return left

def obtain_next_val(disk, left, next_idx):
    if next_idx < len(left):
        next_val = left[next_idx]
    else:
        next_val = (disk - 1)
    return next_val

def check_is_higher(disk, right):
    if disk in right:
        return right
    min_val = min(right)
    if disk > min_val:
        for idx, val in enumerate(right):
            next_idx = idx + 1
            if next_idx < len(right):
                next_val = right[next_idx]
            else:
                next_val = (disk + 1)
            if val < disk < next_val:
                right.insert(idx + 1, disk)
    return right


def solution(list_of_disks, leftIncreasingValues, rightDecreasingValues):
    left = [leftIncreasingValues]
    right = [rightDecreasingValues]
    for disk in list_of_disks:
        original_left = len(left)
        left = check_is_lower(disk, left)
        if original_left == len(left):
            right = check_is_higher(disk, right)
    return len(left) + len(right) - 2


