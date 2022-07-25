input = "110011000111101"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    current_char = string[0]
    count_turn = [0, 0]
    count_turn[int(current_char)] += 1

    for char in string:
        if current_char != char:
            count_turn[int(char)] += 1
            current_char = char

    if count_turn[0] < count_turn[1]:
        count_turn_min = count_turn[0]
    else:
        count_turn_min = count_turn[1]

    print(count_turn)

    return count_turn_min


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)