input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        index = ord(char) - ord('a')
        alphabet_occurrence_array[index] += 1

    max_index = 0
    max_num = alphabet_occurrence_array[max_index]

    for i, num in enumerate(alphabet_occurrence_array):
        if max_num < num:
            max_num = num
            max_index = i

    max_alphabet = chr(ord('a') + max_index)
    return max_alphabet


result = find_max_occurred_alphabet(input)
print(result)