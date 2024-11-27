
# Other possible solutions:
def digital_root_4(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

def digital_root_2(n):
    # ...
    while n>9:
        n=sum(map(int,str(n)))
    return n

def digital_root_3(n):
    root = 0
    for d in str(n):
        root += int(d)
    if len(str(root)) > 1:
        root = digital_root(root)
    return root

def sum_digits(data):
    data["result"] = 0
    for value in list(data["origin"]):
        data["result"] += int(value)
    data["origin"] = str(data["result"])

def digital_root(a_number):
    if a_number == 0 or a_number is None:
        return 0
    return process(a_number) if a_number > 9 else a_number;

def process(a_number):
    result = {"origin": str(a_number), "result": a_number}
    while result["result"] > 9:
        sum_digits(result)
    return result["result"]


