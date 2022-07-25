array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    index_1 = 0
    index_2 = 0
    new_array = []
    while True:
        if array1[index_1] < array2[index_2]:
            new_array.append(array1[index_1])
            index_1 += 1
        else:
            new_array.append(array2[index_2])
            index_2 += 1

        if index_1 >= len(array1):
            new_array.extend(array2[index_2:])
            break

        if index_2 >= len(array2):
            new_array.extend(array1[index_1:])
            break

    return new_array


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!