finding_target = 14.5
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    start_point = 0
    end_point = len(array) - 1

    while start_point <= end_point:
        avg_point = (start_point + end_point) // 2

        if array[avg_point] == target:
            return True
        if array[avg_point] > target:
            end_point = avg_point - 1
        elif array[avg_point] < target:
            start_point = avg_point + 1

        print(start_point, end_point)
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)


def is_existing_target_number_binary_by_recall(target, array, start_point, end_point):
    print(start_point, end_point)
    if start_point > end_point:
        return False

    avg_point = (start_point + end_point) // 2
    if array[avg_point] == target:
        return True
    if array[avg_point] > target:
        return is_existing_target_number_binary_by_recall(target, array, start_point, avg_point - 1)
    elif array[avg_point] < target:
        return is_existing_target_number_binary_by_recall(target, array, avg_point + 1, end_point)


result = is_existing_target_number_binary_by_recall(finding_target, finding_numbers, 0, len(finding_numbers) - 1)
print(result)