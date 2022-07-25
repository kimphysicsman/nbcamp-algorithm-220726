input = "abadabaccandipadfk"


def find_not_repeating_character(string):
    alpha_list = []
    alpha_repeating = []

    for char in string:
        alpha_first = True
        if len(alpha_list) == 0:
            alpha_list.append(char)
            alpha_repeating.append(1)
            continue
        for i, alpha in enumerate(alpha_list):
            if alpha == char:
                alpha_repeating[i] += 1
                alpha_first = False
                break
        if alpha_first:
            alpha_list.append(char)
            alpha_repeating.append(1)

    print(alpha_list)
    print(alpha_repeating)

    for i, num in enumerate(alpha_repeating):
        if num == 1:
            return alpha_list[i]
    return "_"


result = find_not_repeating_character(input)
print(result)