def check_is_lower_in_left(disk, left):
    if disk in left:
        return left
    max_val = max(left)
    if disk < max_val:
        for idx, val in enumerate(left):
            next_idx = idx + 1
            if next_idx < len(left):
                next_val = left[next_idx]
            else:
                next_val = (disk - 1)
            if val > disk >= next_val:
                left.insert(idx+1, disk)
    return left


def solution(list_of_disks, leftIncreasingValues, rightDecreasingValues):
    left = [leftIncreasingValues]
    right = [rightDecreasingValues]
    for disk in list_of_disks:
        original_left = len(left)
        left = check_is_lower_in_left(disk, left)
        if original_left == len(left):
            if disk > right[-1]:
                right.append(disk)

    return len(left) + len(right) - 2


