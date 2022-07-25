input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    max_num = -9999999
    for num in input:
        if max_num < num:
            max_num = num
    return max_num


result = find_max_num(input)
print(result)