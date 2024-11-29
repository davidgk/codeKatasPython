def find_uniq(a_list):
    decrement = len(a_list)-1
    checker = {"unique": "", "cte": "" }
    for idx in range(0, decrement):
        idx = (idx + 1) if idx == decrement else idx
        value = a_list[idx]
        last_value=a_list[decrement]
        if value == last_value:
            decrement-=1
            checker["cte"]=value
        else:
            if value == a_list[decrement-1]:
                return last_value
            return value

# def split_list(a_list):
#     middle = len(a_list) // 2
#     first_half = a_list[0:middle]
#     scnd_half = a_list[middle + 1: len(a_list) - 1]
#     return first_half, scnd_half