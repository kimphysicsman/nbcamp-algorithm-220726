input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    current_num = array[0]
    for i, num in enumerate(array):
        if i == 0:
            continue
        if current_num + num > current_num * num:
            current_num += num
        else:
            current_num *= num
    return current_num


result = find_max_plus_or_multiply(input)
print(result)