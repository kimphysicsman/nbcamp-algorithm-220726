input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    while True:
        end_bool = True
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                end_bool = False
        if end_bool:
            break
    return


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!