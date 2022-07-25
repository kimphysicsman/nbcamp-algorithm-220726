def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for alpha in string:
        if alpha.isalpha():
            index = ord(alpha) - ord('a')
            alphabet_occurrence_array[index] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))