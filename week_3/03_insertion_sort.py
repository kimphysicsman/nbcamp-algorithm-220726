input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    for i in range(len(array)):
        new_index = i
        for j in range(i):
            index = i - j - 1
            if array[index] > array[new_index]:
                array[new_index], array[index] = array[index], array[new_index]
                new_index = index
            else:
                break
    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!