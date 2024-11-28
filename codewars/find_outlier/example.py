# Other solutions:
def find_outlier_02(ints):
    odds = [x for x in ints if x%2!=0]
    evens= [x for x in ints if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

def find_outlier_03(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]


def find_outlier_04(nums):
    base_parity = sum(x % 2 for x in nums[:3]) // 2
    for i in range(len(nums)):
        if nums[i] % 2 != base_parity:
            return nums[i]

def find_outlier_05(integers):
    return next(i for i in integers if i%2 != int(sum(x%2 for x in integers[:3]) > 1))

def check_outlier(a_list):
    sample = a_list[0:3]
    key = get_outlier_key(sample)
    values = list(filter(lambda x: x % 2 == key, a_list))
    return values[0]

def get_outlier_key(sample):
    is_outlier_even = (len(list(filter(lambda x: x % 2 == 0, sample)))) <= 1
    key = 0 if is_outlier_even else 1
    return key


def find_outlier(a_list):
    return check_outlier(a_list) if not len(a_list) <= 2 else -1
